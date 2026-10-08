"""Independently reopen a candidate and compare authored, saved, and baked poses."""

import json
from pathlib import Path
import sys

import bpy
import numpy as np
from mathutils import Matrix

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repair import ROOT, digest, retrieve_matrices
import dance_tools
from animation_export_evaluation import AnimationExportEvaluation
from track_chooser import TrackChooser


def main():
    identifier = sys.argv[sys.argv.index('--') + 1]
    directory = ROOT / '.cache/motion-recovery' / identifier
    report = json.loads((directory / 'checkpoint.json').read_text())
    reference = np.load(directory / 'authored.npz')
    frames, authored = reference['frames'], reference['matrices']
    bpy.ops.wm.open_mainfile(filepath=str(ROOT / report['source']))
    dance_tools.register()
    TrackChooser(bpy.context.scene).apply(identifier)
    scene = bpy.context.scene
    action = bpy.data.actions[identifier]
    rigs = [scene.objects[actor.capitalize() + '.rigify_deform'] for actor in report['performers']]
    controls = [scene.objects[actor.capitalize() + '.rigify'] for actor in report['performers']]
    rate = scene.render.fps / scene.render.fps_base
    assert rate == report['rate'], ('rate', rate)
    assert list(action.frame_range) == report['storedRange']
    assert [[bone.name for bone in rig.pose.bones] for rig in rigs] == report['boneNames']
    assert all(Path(bpy.path.abspath(library.filepath)).is_file() for library in bpy.data.libraries)
    for repair in report['rotationRepairs']:
        assert scene.objects[repair['owner']].pose.bones[repair['bone']].rotation_mode == 'QUATERNION'
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
    evaluation = AnimationExportEvaluation(set(rigs + controls))
    evaluation.prepare()
    try:
        saved = []
        for frame in frames:
            scene.frame_set(int(frame), subframe=frame % 1)
            saved.append(retrieve_matrices(rigs))
        saved = np.array(saved)
        baked = bpy.data.actions[identifier + '.baked']
        for rig in rigs:
            rig.animation_data.action = baked
            rig.animation_data.action_slot = next(slot for slot in baked.slots if slot.identifier == 'OB' + rig.name)
            for bone in rig.pose.bones:
                for constraint in bone.constraints:
                    constraint.mute = True
        playback = []
        for frame in frames:
            scene.frame_set(int(frame), subframe=frame % 1)
            playback.append(retrieve_matrices(rigs))
        playback = np.array(playback)
    finally:
        evaluation.restore()
    assert np.isfinite(saved).all() and np.isfinite(playback).all()
    position_errors = np.linalg.norm(playback[..., :3, 3] - saved[..., :3, 3], axis=-1)
    worst = np.unravel_index(np.argmax(position_errors), position_errors.shape)
    integer = np.isclose(frames % 1, 0)
    measurements = dict(savedSourceMatrixError=float(np.max(np.abs(saved - authored))),
                        bakeIntegerMatrixError=float(np.max(np.abs(playback[integer] - saved[integer]))),
                        bakeSubframePositionError=float(position_errors.max()),
                        worstBakeSample=dict(frame=float(frames[worst[0]]), performer=report['performers'][worst[1]], bone=report['boneNames'][worst[1]][worst[2]]),
                        loopPositionError=float(np.linalg.norm(saved[-1, ..., :3, 3] - saved[0, ..., :3, 3], axis=-1).max()) if report['loop'] else None)
    limits = dict(savedSourceMatrixError=0.0001, bakeIntegerMatrixError=0.0001, bakeSubframePositionError=0.002, loopPositionError=0.001)
    failures = {key: value for key, value in measurements.items() if key in limits and value is not None and value > limits[key]}
    report.update(validation=measurements, limits=limits, failures=failures,
                  validationGeneratorSha256=digest(__file__), stage='saved source and bake validated' if not failures else 'candidate requires refinement')
    (directory / 'checkpoint.json').write_text(json.dumps(report, indent=2) + '\n')
    print('REVIEW', identifier, json.dumps(measurements), 'FAILURES', failures, flush=True)
    assert not failures, (identifier, failures)


if __name__ == '__main__':
    main()
