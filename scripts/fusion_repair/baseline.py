"""Fresh-process Fusion source and baked-deformation diagnostics."""
import json
from pathlib import Path
import sys
import bpy
import numpy as np
from mathutils import Matrix

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/motion_recovery'))
from repair import digest, retrieve_curves, retrieve_matrices
import dance_tools
from track_chooser import TrackChooser
from animation_export_evaluation import AnimationExportEvaluation

identifier = sys.argv[sys.argv.index('--') + 1]
directory = ROOT / '.cache/fusion-repair/baseline' / identifier
directory.mkdir(parents=True, exist_ok=True)
source = ROOT / 'animations/fusion/sources' / (identifier + '.blend')
bpy.ops.wm.open_mainfile(filepath=str(source))
version = list(bpy.data.version)
dance_tools.register()
TrackChooser(bpy.context.scene).apply(identifier)
scene = bpy.context.scene
action = bpy.data.actions[identifier]
rigs = [scene.objects[actor + '.rigify_deform'] for actor in ('Man', 'Woman')]
controls = [scene.objects[actor + '.rigify'] for actor in ('Man', 'Woman')]
for rig in rigs + controls:
    rig.hide_viewport = False
    rig.hide_set(False)
for rig in rigs:
    rig.animation_data.action = None
    rig.animation_data.use_nla = False
    for bone in rig.pose.bones:
        bone.matrix_basis = Matrix.Identity(4)
        for constraint in bone.constraints:
            constraint.mute = False
frames = np.arange(action.frame_range[0], action.frame_range[1] + .01, .5)
curves = {}
for slot in action.slots:
    curves[slot.identifier] = [dict(path=curve.data_path, index=curve.array_index, points=[list(point.co) for point in curve.keyframe_points], interpolation=sorted({point.interpolation for point in curve.keyframe_points})) for curve in retrieve_curves(action, slot)]
(directory / 'curves.json').write_text(json.dumps(curves, indent=2))
evaluation = AnimationExportEvaluation(set(rigs + controls))
evaluation.prepare()
try:
    authored = []
    control_samples = []
    names = ['root', 'torso', 'foot_ik.L', 'foot_ik.R', 'hand_ik.L', 'hand_ik.R']
    for frame in frames:
        scene.frame_set(int(frame), subframe=frame % 1)
        authored.append(retrieve_matrices(rigs))
        graph = bpy.context.evaluated_depsgraph_get()
        control_samples.append([[list((rig.matrix_world @ rig.evaluated_get(graph).pose.bones[name].matrix).translation) for name in names] for rig in controls])
    authored = np.array(authored)
    baked = bpy.data.actions[identifier + '.baked']
    for rig in rigs:
        rig.animation_data.action = baked
        rig.animation_data.action_slot = next(slot for slot in baked.slots if slot.identifier == 'OB' + rig.name)
        for bone in rig.pose.bones:
            bone.matrix_basis = Matrix.Identity(4)
            for constraint in bone.constraints:
                constraint.mute = True
    playback = []
    for frame in frames:
        scene.frame_set(int(frame), subframe=frame % 1)
        playback.append(retrieve_matrices(rigs))
    playback = np.array(playback)
finally:
    evaluation.restore()
errors = np.linalg.norm(playback[..., :3, 3] - authored[..., :3, 3], axis=-1)
worst = np.unravel_index(np.argmax(errors), errors.shape)
report = dict(id=identifier, sourceSha256=digest(source), exportSha256=digest(source.parent.parent / (identifier + '.glb')), sourceVersion=version, blender=bpy.app.version_string,
    rate=scene.render.fps / scene.render.fps_base, storedRange=list(action.frame_range), loop=action.use_cyclic, owners=[slot.identifier for slot in action.slots],
    participants=action.get('player_asset_participants'), properties={key:str(value) for key,value in action.items()},
    maximumBonePositionError=float(errors.max()), integerMatrixError=float(np.abs(playback[::2]-authored[::2]).max()),
    worst=dict(frame=float(frames[worst[0]]), actor=rigs[worst[1]].name, bone=rigs[worst[1]].pose.bones[worst[2]].name),
    boneNames=[[bone.name for bone in rig.pose.bones] for rig in rigs], controlNames=names,
    rotationModes={rig.name:{bone.name:bone.rotation_mode for bone in rig.pose.bones if any(curve['path'].startswith(bone.path_from_id()) for curve in curves['OB'+rig.name])} for rig in controls},
    dependencies={str(Path(bpy.path.abspath(library.filepath)).relative_to(ROOT)):digest(bpy.path.abspath(library.filepath)) for library in bpy.data.libraries},
    sampledFrames=frames.tolist(), units='meters', generatorSha256=digest(__file__))
np.savez_compressed(directory / 'samples.npz', frames=frames, authored=authored, baked=playback, controls=control_samples)
(directory / 'report.json').write_text(json.dumps(report,indent=2)+'\n')
print('BASELINE',identifier,report['maximumBonePositionError'],report['integerMatrixError'],report['worst'],flush=True)
