"""Recheck Salsa support targets, partner contacts, clearance, and wrists."""
import json
import math
from pathlib import Path
import sys

import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'scripts/motion_recovery'), str(Path(__file__).parent)]
from repair import digest
import dance_tools
from animation_export_evaluation import AnimationExportEvaluation
from track_chooser import TrackChooser
from snap_hand import HandSnap
from choreography import SalsaMove, SalsaChoreography


def main():
    identifier = sys.argv[sys.argv.index('--') + 1]
    directory = ROOT / '.cache/motion-recovery' / identifier
    report = json.loads((directory / 'checkpoint.json').read_text())
    bpy.ops.wm.open_mainfile(filepath=str(ROOT / report['source']))
    dance_tools.register()
    scene = bpy.context.scene
    TrackChooser(scene).apply(identifier)
    action = bpy.data.actions[identifier]
    move = SalsaMove(**json.loads(action['Salsa']))
    choreography = SalsaChoreography(move)
    rigs = {actor: scene.objects[name + '.rigify'] for actor, name in (('player', 'Man'), ('partner', 'Woman'))}
    deform = [scene.objects[name + '.rigify_deform'] for name in ('Man', 'Woman')]
    hands = {(actor, side): HandSnap(bpy.context, rig, side) for actor, rig in rigs.items() for side in 'LR'}
    evaluation = AnimationExportEvaluation(set(rigs.values()) | set(deform))
    evaluation.prepare()
    plant, palm, bend, speed, clearance, contacts = 0, 0, 0, 0, float('inf'), 0
    previous = {}
    scene.frame_set(0)
    initial = {(actor, side): rig.pose.bones['foot_ik.' + side].matrix.translation.z for actor, rig in rigs.items() for side in 'LR'}
    try:
        for frame in report['sampledFrames']:
            scene.frame_set(int(frame), subframe=frame % 1)
            count = frame / report['rate'] * 144 / 60
            bodies = []
            for actor, rig in rigs.items():
                bodies.append(rig.pose.bones['torso'].matrix.translation.copy())
                for side, label in (('L', 'left'), ('R', 'right')):
                    foot = choreography.retrieve_foot(actor, label, count)
                    after = choreography.retrieve_foot(actor, label, min(move.counts, count + .01))
                    if max(abs(first-last) for first, last in zip(foot, after)) < 1e-8:
                        target = Vector((foot[0], foot[1], initial[actor, side] + foot[2]))
                        plant = max(plant, (rig.pose.bones['foot_ik.' + side].matrix.translation - target).length)
                    forearm, hand = [rig.pose.bones[name + side] for name in ('ORG-forearm.', 'ORG-hand.')]
                    bend = max(bend, math.degrees((forearm.tail-forearm.head).angle(hand.tail-hand.head)))
                    rotation = hand.matrix.to_quaternion()
                    if (actor, side) in previous:
                        angle = math.degrees(previous[actor, side].rotation_difference(rotation).angle)
                        speed = max(speed, min(angle, 360-angle) * report['rate'] / .5)
                    previous[actor, side] = rotation.copy()
            separation = bodies[0] - bodies[1]
            separation.z = 0
            clearance = min(clearance, separation.length)
            held = move.connection in ('open', 'double', 'closed', 'turn') or (move.connection == 'release' and (count <= 1 or count >= move.counts - 1))
            if held:
                for leader, follower in ([('L', 'R'), ('R', 'L')] if move.connection == 'double' else [('L', 'R')]):
                    first, second = hands['player', leader], hands['partner', follower]
                    gap = ((first.retrieve_hand_pose() @ first.wrist.inverted()).translation - (second.retrieve_hand_pose() @ second.wrist.inverted()).translation).length
                    palm = max(palm, gap)
                    contacts += 1
    finally:
        evaluation.restore()
    result = dict(sourceSha256=report['sourceSha256'], generatorSha256=digest(__file__), sampledFrames=len(report['sampledFrames']),
                  contactSamples=contacts, plantTargetError=plant, maximumPalmGap=palm, bodyCenterClearance=clearance,
                  maximumWristBend=bend, maximumWristSpeed=speed, units='meters, degrees, degrees/second',
                  limits=dict(plantTargetError=.008, maximumPalmGap=.035, bodyCenterClearance=.38, maximumWristBend=85, maximumWristSpeed=1560),
                  passed=plant < .008 and palm < .035 and clearance > .38 and bend < 85 and speed < 1560)
    (directory / 'contacts.json').write_text(json.dumps(result, indent=2) + '\n')
    print('CONTACTS', identifier, json.dumps(result), flush=True)
    assert result['passed'], result


if __name__ == '__main__':
    main()
