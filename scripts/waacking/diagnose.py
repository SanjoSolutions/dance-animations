"""Inspect the saved Waacking controls and fractional-frame deformation bake."""
import json
import math
from pathlib import Path
import sys

import bpy
import numpy as np
from mathutils import Matrix

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/motion_recovery'))
from repair import bind_source, digest, retrieve_curves, retrieve_matrices
import dance_tools
from animation_export_evaluation import AnimationExportEvaluation
from track_chooser import TrackChooser


def main():
    identifier = sys.argv[sys.argv.index('--') + 1]
    source = ROOT / 'animations/waacking/sources' / (identifier + '.blend')
    bpy.ops.wm.open_mainfile(filepath=str(source))
    version = list(bpy.data.version)
    dance_tools.register()
    TrackChooser(bpy.context.scene).apply(identifier)
    action = bpy.data.actions[identifier]
    actor = 'Man' if '_man_' in identifier else 'Woman'
    control = bpy.context.scene.objects[actor + '.rigify']
    rig = bpy.context.scene.objects[actor + '.rigify_deform']
    curves = retrieve_curves(action, action.slots[0])
    controls = {}
    for path in sorted({curve.data_path for curve in curves if 'pose.bones' in curve.data_path}):
        name = path.split('"')[1]
        bone = control.pose.bones[name]
        controls[path] = dict(mode=bone.rotation_mode, keys=max(len(curve.keyframe_points) for curve in curves if curve.data_path == path))
    bind_source(action)
    evaluation = AnimationExportEvaluation({control, rig})
    evaluation.prepare()
    frames = np.arange(action.frame_range[0], action.frame_range[1] + .01, .25)
    samples = []
    for frame in frames:
        bpy.context.scene.frame_set(int(frame), subframe=frame % 1)
        samples.append(retrieve_matrices([rig]))
    baked = next(item for item in bpy.data.actions if item.name == identifier + '.baked')
    rig.animation_data.action = baked
    rig.animation_data.action_slot = next(slot for slot in baked.slots if slot.identifier == 'OB' + rig.name)
    for bone in rig.pose.bones:
        for constraint in bone.constraints:
            constraint.mute = True
    positions, rotations, steps = [], [], []
    for index, frame in enumerate(frames):
        bpy.context.scene.frame_set(int(frame), subframe=frame % 1)
        actual = retrieve_matrices([rig])[0]
        expected = samples[index][0]
        for joint, bone in enumerate(rig.pose.bones):
            error = np.linalg.norm(actual[joint, :3, 3] - expected[joint, :3, 3])
            angle = Matrix(actual[joint]).to_quaternion().rotation_difference(Matrix(expected[joint]).to_quaternion()).angle
            angle = math.degrees(min(angle, 2 * math.pi - angle))
            positions.append((float(error), float(frame), bone.name))
            rotations.append((angle, float(frame), bone.name))
            if index:
                angle = Matrix(samples[index-1][0][joint]).to_quaternion().rotation_difference(Matrix(expected[joint]).to_quaternion()).angle
                steps.append((math.degrees(min(angle, 2 * math.pi - angle)), float(frame), bone.name))
    evaluation.restore()
    report = dict(id=identifier, sourceSha256=digest(source), blender=bpy.app.version_string, sourceVersion=version,
                  frameRange=list(action.frame_range), rate=bpy.context.scene.render.fps / bpy.context.scene.render.fps_base,
                  controls=controls, maximumPosition=max(positions), maximumRotation=max(rotations), maximumStep=max(steps),
                  armSteps=sorted((step for step in steps if 'upper_arm' in step[2]), reverse=True)[:20],
                  dependencies={library.filepath: str(Path(bpy.path.abspath(library.filepath)).resolve()) for library in bpy.data.libraries})
    directory = ROOT / '.cache/motion-recovery' / identifier
    directory.mkdir(parents=True, exist_ok=True)
    (directory / 'baseline.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key:value for key,value in report.items() if key not in ('controls','dependencies')}, indent=2))


if __name__ == '__main__':
    main()
