"""Review saved Hustle contacts and compare every deformation bone with its bake.

Run through Blender 5.2 with optional clip IDs after --.
Results are written to .cache/hustle-polish/validation.json.
"""

import json
import math
import hashlib
import subprocess
import tempfile
import struct
from pathlib import Path
import sys

import bpy
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
BASELINE = '7b8535fa37873dca51ac9f07b85e82918d5fa9b3'
sys.path.insert(0, str(ROOT / 'scripts'))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import dance_tools
from polish import GripTiming
from snap_hand import HandSnap
from animation_export_evaluation import AnimationExportEvaluation


def retrieve_body_signature(action, follows_elbow=False):
    controls = tuple('pose.bones["' + prefix for prefix in
                     ('hand_ik.', 'hand_tweak.', 'f_index.', 'f_middle.', 'f_ring.', 'f_pinky.', 'thumb.'))
    digest = hashlib.sha256()
    for slot in action.slots:
        curves = [curve for layer in action.layers for strip in layer.strips
                  for bag in strip.channelbags if bag.slot_handle == slot.handle
                  for curve in bag.fcurves if not curve.data_path.startswith(controls)
                  and not (follows_elbow and slot.identifier == 'OBWoman.rigify'
                           and curve.data_path == 'pose.bones["upper_arm_ik_target.R"].location')]
        digest.update(slot.identifier.encode())
        for curve in sorted(curves, key=lambda curve: (curve.data_path, curve.array_index)):
            digest.update(curve.data_path.encode())
            digest.update(struct.pack('<I', curve.array_index))
            for point in curve.keyframe_points:
                digest.update(struct.pack('<6f', *point.co, *point.handle_left, *point.handle_right))
                digest.update(point.interpolation.encode())
    return digest.hexdigest()


def compare_original(action, record):
    follows_elbow = GripTiming(record['id']).follows_elbow('Woman', 'R')
    current = retrieve_body_signature(action, follows_elbow)
    with tempfile.TemporaryDirectory(prefix='hustle-original-') as directory:
        source = Path(directory) / 'original.blend'
        with source.open('wb') as stream:
            subprocess.run(['git', 'show', BASELINE + ':' + record['sourceFile']], cwd=ROOT, stdout=stream, check=True)
        with bpy.data.libraries.load(str(source)) as (_available, loaded):
            loaded.actions = [record['id']]
        original = loaded.actions[0]
        assert retrieve_body_signature(original, follows_elbow) == current, record['id']
        for name in ('Tempo', 'Counts', 'Loop Frames', 'Hustle Clip', 'Hustle Library', 'Description'):
            assert action.get(name) == original.get(name), (record['id'], name)
        bpy.data.actions.remove(original)
    return current


def retrieve_matrices(rigs):
    graph = bpy.context.evaluated_depsgraph_get()
    return np.array([[list(row) for bone in rig.evaluated_get(graph).pose.bones for row in bone.matrix]
                     for rig in rigs])


def review(record):
    bpy.ops.wm.open_mainfile(filepath=str(ROOT / record['sourceFile']))
    dance_tools.register()
    scene = bpy.context.scene
    action = bpy.data.actions[record['id']]
    assert action.get('Hustle Hand Polish'), record['id']
    body_signature = compare_original(action, record)
    rigs = [scene.objects[actor + '.rigify_deform'] for actor in ('Man', 'Woman')]
    controls = [scene.objects[actor + '.rigify'] for actor in ('Man', 'Woman')]
    hands = {(actor, side): HandSnap(bpy.context, rig, side)
             for actor, rig in zip(('Man', 'Woman'), controls) for side in 'LR'}
    timing = GripTiming(action.name)
    evaluation = AnimationExportEvaluation(set(rigs + controls))
    evaluation.prepare()
    try:
        start, end = action.frame_range
        frames = np.arange(start, end + .01, .5).tolist()
        native = []
        maximum_gap = 0.0
        maximum_wrist_step = 0.0
        previous = {}
        worst_wrist = None
        worst_gap_frame = start
        for frame in frames:
            scene.frame_set(int(frame), subframe=frame % 1)
            matrices = retrieve_matrices(rigs)
            assert np.isfinite(matrices).all(), record['id']
            if frame.is_integer():
                native.append((frame, matrices))
            for leader, follower, weight, _heading in timing.retrieve_contacts(frame):
                if weight == 1:
                    first = hands['Man', leader]
                    second = hands['Woman', follower]
                    gap = ((first.retrieve_hand_pose() @ first.wrist.inverted()).translation
                           - (second.retrieve_hand_pose() @ second.wrist.inverted()).translation).length
                    if gap > maximum_gap:
                        maximum_gap, worst_gap_frame = gap, frame
            for pair, hand in hands.items():
                rotation = hand.retrieve_hand_pose().to_quaternion()
                if pair in previous:
                    difference = rotation.rotation_difference(previous[pair]).angle
                    difference = min(difference, 2 * math.pi - difference)
                    if difference > maximum_wrist_step:
                        maximum_wrist_step, worst_wrist = difference, (pair, frame)
                previous[pair] = rotation
        baked = bpy.data.actions[action.name + '.baked']
        for rig in rigs:
            rig.animation_data.use_nla = False
            rig.animation_data.action = baked
            rig.animation_data.action_slot = next(slot for slot in baked.slots if slot.identifier == 'OB' + rig.name)
            for bone in rig.pose.bones:
                for constraint in bone.constraints:
                    constraint.mute = True
        maximum_bake_error = 0.0
        for frame, expected in native:
            scene.frame_set(int(frame))
            maximum_bake_error = max(maximum_bake_error, float(np.max(np.abs(retrieve_matrices(rigs) - expected))))
        assert maximum_bake_error < 0.0001, (record['id'], maximum_bake_error)
        assert maximum_gap < 0.025, (record['id'], 'Palm gap', maximum_gap, worst_gap_frame)
        assert maximum_wrist_step < 0.6, (record['id'], 'Wrist step', maximum_wrist_step, worst_wrist)
        return dict(id=record['id'], sampledFrames=len(frames), maximumPalmGap=maximum_gap,
                    worstGapFrame=worst_gap_frame, maximumWristStep=maximum_wrist_step,
                    maximumBakeError=maximum_bake_error, worstWristStep=worst_wrist, bodyChannelSha256=body_signature, deformationBones=sum(len(rig.pose.bones) for rig in rigs))
    finally:
        evaluation.restore()


def main():
    requested = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    records = [entry for entry in catalog['animations'] if entry['style'] == 'new_york_hustle'
               and (entry['id'] in requested or not requested)]
    destination = ROOT / '.cache/hustle-polish/validation.json'
    previous = json.loads(destination.read_text()) if requested and destination.is_file() else []
    results = {entry['id']: entry for entry in previous}
    for record in records:
        result = review(record)
        results[record['id']] = result
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(sorted(results.values(), key=lambda entry: entry['id']), indent=2) + '\n')
        print('VALIDATED', json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
