"""Add arm, wrist, support, and all-bone angular review to native source checks."""
import json
import math
from pathlib import Path
import sys

import bpy
import numpy as np
from mathutils import Matrix

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/motion_recovery'))
import validate
from repair import digest, retrieve_matrices
from animation_export_evaluation import AnimationExportEvaluation


def angle(first, second):
    value = first.rotation_difference(second).angle
    return math.degrees(min(value, 2 * math.pi - value))


def main():
    identifier = sys.argv[sys.argv.index('--') + 1]
    try:
        validate.main()
    except AssertionError:
        pass
    directory = ROOT / '.cache/motion-recovery' / identifier
    report = json.loads((directory / 'checkpoint.json').read_text())
    reference = np.load(directory / 'authored.npz')
    authored = reference['matrices'][:, 0]
    frames = reference['frames']
    scene = bpy.context.scene
    actor = report['performers'][0].capitalize()
    control, rig = [scene.objects[actor + suffix] for suffix in ('.rigify', '.rigify_deform')]
    evaluation = AnimationExportEvaluation({control, rig})
    evaluation.prepare()
    rotation_error = (0, 0, '')
    endpoint_error = (0, 0, '')
    maximum_step = (0, 0, '')
    bend, reach = (0, 0, ''), (0, 0, '')
    feet = {side: [] for side in 'LR'}
    previous = None
    try:
        for index, frame in enumerate(frames):
            scene.frame_set(int(frame), subframe=frame % 1)
            playback = retrieve_matrices([rig])[0]
            current = []
            for joint, bone in enumerate(rig.pose.bones):
                expected = Matrix(authored[index, joint])
                actual = Matrix(playback[joint])
                rotation_error = max(rotation_error, (angle(expected.to_quaternion(), actual.to_quaternion()), float(frame), bone.name))
                tail = np.array([0, bone.length, 0, 1])
                endpoint_error = max(endpoint_error, (float(np.linalg.norm((authored[index, joint] @ tail - playback[joint] @ tail)[:3])), float(frame), bone.name))
                current.append(expected.to_quaternion())
                if previous:
                    maximum_step = max(maximum_step, (angle(previous[joint], current[-1]), float(frame), bone.name))
            previous = current
            for side in 'LR':
                forearm, hand, target = [control.pose.bones[name + side] for name in ('ORG-forearm.', 'ORG-hand.', 'hand_ik.')]
                bend = max(bend, (math.degrees((forearm.tail-forearm.head).angle(hand.tail-hand.head)), float(frame), side))
                reach = max(reach, ((hand.head-target.head).length, float(frame), side))
                feet[side].append(list(control.pose.bones['foot_ik.' + side].head))
    finally:
        evaluation.restore()
    support = {}
    for side, positions in feet.items():
        positions = np.array(positions)
        speed = np.linalg.norm(np.diff(positions, axis=0), axis=-1) * report['rate'] / .5
        support[side] = dict(minimumControlHeight=float(positions[:,2].min()), maximumControlHeight=float(positions[:,2].max()),
                             maximumControlSpeed=float(speed.max()), stationarySamples=int((speed < .01).sum()),
                             coverage='Control speed and height; standing support through the complete rotation loop')
    result = dict(sourceSha256=report['sourceSha256'], exportSha256=report['exportSha256'], generatorSha256=digest(__file__),
                  frames=frames.tolist(), bones=len(rig.pose.bones), units='meters and degrees',
                  maximumBakeRotation=rotation_error, maximumBakeTailError=endpoint_error, maximumAuthoredAngularStep=maximum_step,
                  maximumWristBend=bend, maximumHandReachError=reach, footControls=support,
                  actionMetadata={key: str(value) for key,value in bpy.data.actions[identifier].items() if key in ('Waacking','Waacking Arm Repair','Waacking Sole Calibration','Motion Recovery')},
                  ownerSlots=[slot.identifier for slot in bpy.data.actions[identifier].slots],
                  bakedSlots=[slot.identifier for slot in bpy.data.actions[identifier+'.baked'].slots],
                  controlTracks=[dict(name=track.name, strips=[dict(name=strip.name, start=strip.frame_start, end=strip.frame_end,
                      influence=strip.influence, slot=strip.action_slot.identifier) for strip in track.strips]) for track in control.animation_data.nla_tracks],
                  controlRotationModes={bone.name:bone.rotation_mode for bone in control.pose.bones},
                  limits=dict(maximumBakeRotation=3, maximumBakeTailError=.006, maximumAuthoredAngularStep=20, maximumWristBend=85, maximumHandReachError=.006),
                  coverage=dict(bones='every deform bone including fingers and toes', bake='live follow constraints muted',
                                contacts='solo foot controls; MPFB sole geometry in surfaces.json', clearance='visual and surface review pending'))
    metrics = dict(maximumBakeRotation=rotation_error[0], maximumBakeTailError=endpoint_error[0], maximumAuthoredAngularStep=maximum_step[0], maximumWristBend=bend[0], maximumHandReachError=reach[0])
    result['failures'] = {name:value for name,value in metrics.items() if value > result['limits'][name]}
    result['failures'].update(report.get('failures', {}))
    result['passed'] = not result['failures']
    (directory / 'motion-review.json').write_text(json.dumps(result, indent=2) + '\n')
    print('MOTION_REVIEW', identifier, json.dumps(metrics), result['failures'], flush=True)
    assert result['passed'], result['failures']


if __name__ == '__main__':
    main()
