"""Repair saved control rotations and generate native, higher-rate candidates.

Blender 5.2 --background --factory-startup --python-exit-code 1
--python scripts/motion_recovery/repair.py -- CLIP_ID
Candidates and per-clip checkpoints live in .cache/motion-recovery.
"""

import hashlib
import json
from pathlib import Path
import sys

import bpy
import numpy as np
from mathutils import Euler, Matrix

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import dance_tools
from animation_export_evaluation import AnimationExportEvaluation
from animation_files import TRACKS_PROPERTY
from track_chooser import TrackChooser


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def retrieve_curves(action, slot):
    return [curve for layer in action.layers for strip in layer.strips
            for bag in strip.channelbags if bag.slot_handle == slot.handle
            for curve in bag.fcurves]


def retrieve_matrices(rigs):
    graph = bpy.context.evaluated_depsgraph_get()
    return np.array([[[list(row) for row in rig.matrix_world @ bone.matrix]
                      for bone in rig.evaluated_get(graph).pose.bones] for rig in rigs])


def bind_source(action):
    """Select each source slot while retaining the native rig drivers."""
    scene = bpy.context.scene
    for actor in ('Man', 'Woman'):
        for suffix in ('.rigify', '.rigify_deform'):
            rig = scene.objects[actor + suffix]
            rig.hide_viewport = False
            rig.hide_set(False)
            data = rig.animation_data_create()
            data.use_tweak_mode = False
            data.action = None
            data.use_nla = False
            for track in list(data.nla_tracks):
                data.nla_tracks.remove(track)
            if suffix == '.rigify_deform':
                for bone in rig.pose.bones:
                    bone.matrix_basis = Matrix.Identity(4)
                    for constraint in bone.constraints:
                        constraint.mute = False
    for slot in action.slots:
        owner = scene.objects[slot.identifier[2:]]
        owner.animation_data.action = action
        owner.animation_data.action_slot = slot
    bpy.context.view_layer.update()


class ConstantRotationRepair:
    """Express held Euler poses in the shared control's quaternion mode."""

    def __init__(self, action):
        self.action = action

    def apply(self):
        repairs = []
        for slot in self.action.slots:
            owner = bpy.context.scene.objects[slot.identifier[2:]]
            curves = retrieve_curves(self.action, slot)
            paths = sorted({curve.data_path for curve in curves if curve.data_path.endswith('.rotation_euler')})
            for path in paths:
                bone = owner.pose.bones[path.split('"')[1]]
                if bone.rotation_mode == 'QUATERNION':
                    selected = sorted((curve for curve in curves if curve.data_path == path), key=lambda curve: curve.array_index)
                    if len(selected) != 3 or any(len(curve.keyframe_points) != 1 for curve in selected):
                        raise ValueError(f'Animated Euler control requires a sampled conversion: {owner.name}/{bone.name}')
                    quaternion_path = bone.path_from_id('rotation_quaternion')
                    if any(curve.data_path == quaternion_path for curve in curves):
                        raise ValueError(f'Review overlapping rotation representations: {owner.name}/{bone.name}')
                    angles = tuple(curve.keyframe_points[0].co.y for curve in selected)
                    quaternion = Euler(angles, 'XYZ').to_quaternion()
                    for layer in self.action.layers:
                        for strip in layer.strips:
                            for bag in strip.channelbags:
                                if bag.slot_handle == slot.handle:
                                    for curve in selected:
                                        bag.fcurves.remove(curve)
                    for component, value in enumerate(quaternion):
                        curve = self.action.fcurve_ensure_for_datablock(owner, quaternion_path, index=component, group_name=bone.name)
                        point = curve.keyframe_points.insert(self.action.frame_range[0], value)
                        point.interpolation = 'CONSTANT'
                    bone.rotation_quaternion = quaternion
                    repairs.append(dict(owner=owner.name, bone=bone.name, euler=list(angles), quaternion=list(quaternion)))
        return repairs


def retime(action, factor):
    """Preserve beat timing while increasing native bake and export sampling."""
    start, end = action.frame_range
    for slot in action.slots:
        for curve in retrieve_curves(action, slot):
            for point in curve.keyframe_points:
                coordinate, left, right = point.co.copy(), point.handle_left.copy(), point.handle_right.copy()
                point.co.x = coordinate.x * factor
                point.handle_left.x, point.handle_right.x = left.x * factor, right.x * factor
            curve.update()
    for marker in action.pose_markers:
        marker.frame = round(marker.frame * factor)
    action.frame_start, action.frame_end = start * factor, end * factor
    if 'Loop Frames' in action:
        action['Loop Frames'] *= factor
    bpy.context.scene.render.fps = round(bpy.context.scene.render.fps * factor)
    action['animation_frame_rate'] = [bpy.context.scene.render.fps, bpy.context.scene.render.fps_base]
    bpy.context.scene.frame_start = int(action.frame_start)
    bpy.context.scene.frame_end = int(action.frame_end) - int(action.use_cyclic)


def main(refinement=None, sampling=2):
    identifier = sys.argv[sys.argv.index('--') + 1]
    record = next(entry for entry in json.loads((ROOT / 'catalog.json').read_text())['animations'] if entry['id'] == identifier)
    directory = ROOT / '.cache/motion-recovery' / identifier
    directory.mkdir(parents=True, exist_ok=True)
    source = ROOT / record['sourceFile']
    bpy.ops.wm.open_mainfile(filepath=str(source))
    dance_tools.register()
    TrackChooser(bpy.context.scene).apply(identifier)
    action = bpy.data.actions[identifier]
    original_rate = bpy.context.scene.render.fps / bpy.context.scene.render.fps_base
    original_range = list(action.frame_range)
    bind_source(action)
    for candidate in list(bpy.data.actions):
        if candidate.name in (identifier + '.baked', identifier + '_baked'):
            bpy.data.actions.remove(candidate)
    repairs = ConstantRotationRepair(action).apply()
    action['player_asset_participants'] = 'BOTH' if len(record['performers']) == 2 else 'PLAYER' if record['performers'] == ['man'] else 'PARTNER'
    action['Motion Recovery'] = 'Native quaternion controls; dense sampling; procedural study'
    action['animation_loop_end_exclusive'] = bool(action.use_cyclic)
    if refinement:
        refinement.apply(action)
    retime(action, max(1.0, 24 * sampling / bpy.context.scene.render.fps))
    action[TRACKS_PROPERTY] = '[]'
    rigs = [bpy.context.scene.objects[actor.capitalize() + '.rigify_deform'] for actor in record['performers']]
    controls = [bpy.context.scene.objects[actor.capitalize() + '.rigify'] for actor in record['performers']]
    evaluation = AnimationExportEvaluation(set(rigs + controls))
    evaluation.prepare()
    try:
        frames = np.arange(action.frame_start, action.frame_end + .01, .5)
        reference = []
        for frame in frames:
            bpy.context.scene.frame_set(int(frame), subframe=frame % 1)
            reference.append(retrieve_matrices(rigs))
        reference = np.array(reference)
        assert np.isfinite(reference).all(), identifier
        np.savez_compressed(directory / 'authored.npz', frames=frames, matrices=reference)
        output = dance_tools.export_action(action, directory / (identifier + '.glb'), update_catalog=False)
    finally:
        evaluation.restore()
    saved = output.parent / 'sources' / (identifier + '.blend')
    report = dict(id=identifier, style=record['style'], baselineSource=digest(source), baselineExport=digest(ROOT / record['file']),
                  sourceSha256=digest(saved), exportSha256=digest(output), source=str(saved.relative_to(ROOT)), export=str(output.relative_to(ROOT)),
                  originalRate=original_rate, originalRange=original_range, rate=bpy.context.scene.render.fps / bpy.context.scene.render.fps_base,
                  storedRange=list(action.frame_range), loop=action.use_cyclic, rotationRepairs=repairs,
                  boneNames=[[bone.name for bone in rig.pose.bones] for rig in rigs],
                  performers=record['performers'], sampledFrames=frames.tolist(),
                  dependencies={str(path.relative_to(ROOT)): digest(path) for path in
                                (ROOT / 'animations/shared_scene_data.blend', ROOT / 'assets/characters/mpfb-characters.blend', ROOT / 'assets/characters/rig-schema.json')},
                  generatorSha256=digest(__file__), blender=bpy.app.version_string, stage='candidate exported')
    if refinement:
        import inspect
        report['refinementGeneratorSha256'] = digest(inspect.getfile(type(refinement)))
        calibration = Path(__file__).parent / 'sole_calibration.py'
        report['calibrationGeneratorSha256'] = digest(calibration)
    (directory / 'checkpoint.json').write_text(json.dumps(report, indent=2) + '\n')
    print('CANDIDATE', identifier, len(repairs), flush=True)


if __name__ == '__main__':
    main()
