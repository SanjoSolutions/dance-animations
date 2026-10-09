"""Measure saved Fusion support, calibrated palms, reach, and wrist motion."""
import json
import math
from pathlib import Path
import sys
import bpy
import numpy as np
from mathutils import Matrix

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/motion_recovery'))
from repair import digest
import dance_tools
from track_chooser import TrackChooser
from animation_export_evaluation import AnimationExportEvaluation
from snap_hand import HandSnap

identifier = sys.argv[sys.argv.index('--') + 1]
directory = ROOT / '.cache/motion-recovery' / identifier
report = json.loads((directory / 'checkpoint.json').read_text())
bpy.ops.wm.open_mainfile(filepath=str(ROOT / report['source']))
dance_tools.register()
scene = bpy.context.scene
TrackChooser(scene).apply(identifier)
action = bpy.data.actions[identifier]
plan = json.loads(action['Fusion support plan'])
rigs = [scene.objects[name + '.rigify'] for name in ('Man', 'Woman')]
deforms = [scene.objects[name + '.rigify_deform'] for name in ('Man', 'Woman')]
for rig in rigs + deforms:
    rig.hide_viewport = False
    rig.hide_set(False)
for rig in deforms:
    rig.animation_data.action = None
    rig.animation_data.use_nla = False
    for bone in rig.pose.bones:
        bone.matrix_basis = Matrix.Identity(4)
        for constraint in bone.constraints:
            constraint.mute = False
hands = [[HandSnap(bpy.context, rig, side) for side in 'LR'] for rig in rigs]
evaluation = AnimationExportEvaluation(set(rigs + deforms))
evaluation.prepare()
feet = []
for actor, rig in enumerate(rigs):
    for side in 'LR':
        feet.append(dict(actor=actor, side=side, control=rig.pose.bones['foot_ik.' + side],
                         bones=[deforms[actor].pose.bones['DEF-' + part + '.' + side] for part in ('foot', 'toe')],
                         intervals=plan['supports'][rig.name + '/' + side]))
positions = [[] for _ in feet]
joints = [[] for _ in feet]
palms, wrist_angles, wrist_rotations, reach = [], [], [], []
try:
    for frame in report['sampledFrames']:
        scene.frame_set(int(frame), subframe=frame % 1)
        palms.append([[list((rig.matrix_world @ hand.retrieve_hand_pose() @ hand.wrist.inverted()).translation) for hand in actor_hands] for rig, actor_hands in zip(rigs, hands)])
        angles, rotations, distances = [], [], []
        for rig in rigs:
            for side in 'LR':
                forearm, hand = [rig.pose.bones[name + side] for name in ('ORG-forearm.', 'ORG-hand.')]
                angles.append(math.degrees((forearm.tail - forearm.head).angle(hand.tail - hand.head)))
                rotations.append(list(hand.matrix.to_quaternion()))
                distances.append((rig.pose.bones['hand_ik.' + side].matrix.translation - hand.head).length)
        wrist_angles.append(angles)
        wrist_rotations.append(rotations)
        reach.append(distances)
        for index, foot in enumerate(feet):
            positions[index].append(list((rigs[foot['actor']].matrix_world @ foot['control'].matrix).translation))
            joints[index].append([list(deforms[foot['actor']].matrix_world @ point) for bone in foot['bones'] for point in (bone.head, bone.tail)])
finally:
    evaluation.restore()
frames = np.array(report['sampledFrames']) * 24 / report['rate']
results = []
for foot, controls, bones in zip(feet, positions, joints):
    intervals = []
    for start, end in foot['intervals']:
        selected = (frames >= start) & (frames <= end)
        control = np.array(controls)[selected]
        bone = np.array(bones)[selected]
        intervals.append(dict(start=start, end=end, samples=int(selected.sum()), controlDrift=float(np.linalg.norm(control - control[0],axis=-1).max()),
                              deformDrift=float(np.linalg.norm(bone - bone[0], axis=-1).max())))
    results.append(dict(actor=report['performers'][foot['actor']], side=foot['side'], intervals=intervals))
palms = np.array(palms)
pairs = []
for leader in range(2):
    for follower in range(2):
        gap = np.linalg.norm(palms[:, 0, leader] - palms[:, 1, follower], axis=-1)
        pairs.append(dict(man='LR'[leader], woman='LR'[follower], initial=float(gap[0]), maximum=float(gap.max()), minimum=float(gap.min())))
connected = [pair for pair in pairs if pair['initial'] < .08]
maximum_control = max(interval['controlDrift'] for foot in results for interval in foot['intervals'])
maximum_deform = max(interval['deformDrift'] for foot in results for interval in foot['intervals'])
result = dict(id=identifier, sourceSha256=report['sourceSha256'], generatorSha256=digest(__file__), plan=plan,
              sampledFrames=report['sampledFrames'], units='meters and degrees', feet=results,
              maximumControlPlantDrift=maximum_control, maximumDeformPlantDrift=maximum_deform,
              palmPairs=pairs, connectedPairs=connected, maximumWristBend=float(np.max(wrist_angles)), maximumHandTargetReachError=float(np.max(reach)),
              limits=dict(plantDrift=.003, palmGap=.035), coverage=dict(support='complete declared intervals', palms='all four pairings; initial proximity identifies intended holds',
              skin='actual-model runtime review', clearance='visual review; geometric intersection coverage pending'),
              passed=maximum_control<=.003 and maximum_deform<=.003 and bool(connected) and max(pair['maximum'] for pair in connected)<=.035)
(directory / 'contacts.json').write_text(json.dumps(result,indent=2)+'\n')
print('CONTACTS', identifier, maximum_control, maximum_deform, pairs, flush=True)
# Export the independent authored reference for the existing actual-model checker.
from mathutils import Matrix
reference = np.load(directory / 'authored.npz')['matrices']
reference[..., :3, 3].astype('<f4').tofile(directory / 'runtime-positions.bin')
axis_transform = np.array([[1,0,0],[0,0,1],[0,-1,0]])
rotations = reference[..., :3, :3].copy()
rotations /= np.linalg.norm(rotations, axis=-2, keepdims=True)
quaternions = []
for matrix in rotations.reshape(-1,3,3):
    quaternion = Matrix(axis_transform @ matrix).to_quaternion()
    quaternions.append([quaternion.x,quaternion.y,quaternion.z,quaternion.w])
np.array(quaternions,dtype='<f4').tofile(directory / 'runtime-rotations.bin')
(directory / 'runtime-reference.json').write_text(json.dumps(dict(positionsFile='runtime-positions.bin',rotationsFile='runtime-rotations.bin',shape=list(reference.shape[:-2]))))
