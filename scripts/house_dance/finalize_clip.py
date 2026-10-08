"""Install a validated source/export pair and verify its relocated native playback."""
import hashlib
import json
import math
from pathlib import Path
import shutil
import struct
import sys

import bpy
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import dance_tools
from animation_export_evaluation import AnimationExportEvaluation
from track_chooser import TrackChooser


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def retrieve_signature(name):
    signature = hashlib.sha256()
    for action_name in (name, name + '.baked'):
        action = bpy.data.actions[action_name]
        signature.update(action_name.encode())
        signature.update(struct.pack('<2f', *action.frame_range))
        for slot in action.slots:
            signature.update(slot.identifier.encode())
            for layer in action.layers:
                for strip in layer.strips:
                    bag = strip.channelbag(slot)
                    if bag:
                        for curve in sorted(bag.fcurves, key=lambda curve: (curve.data_path, curve.array_index)):
                            signature.update(curve.data_path.encode())
                            signature.update(struct.pack('<I', curve.array_index))
                            for point in curve.keyframe_points:
                                signature.update(struct.pack('<6f', *point.co, *point.handle_left, *point.handle_right))
                                signature.update(point.interpolation.encode())
    return signature.hexdigest()


def retrieve_playback(name):
    scene = bpy.context.scene
    TrackChooser(scene).apply(name)
    actor = name.split('_')[1].capitalize()
    rigs = [scene.objects[actor + suffix] for suffix in ('.rigify', '.rigify_deform')]
    for rig in rigs:
        rig.hide_viewport = False
        rig.hide_set(False)
    evaluation = AnimationExportEvaluation(set(rigs))
    evaluation.prepare()
    samples = []
    try:
        for frame in (0, .1, 12.25, 24.5, 48, 72.75, 95.9, 96):
            scene.frame_set(math.floor(frame), subframe=frame % 1)
            rig = rigs[1].evaluated_get(bpy.context.evaluated_depsgraph_get())
            samples.append(np.array([np.array(rig.matrix_world @ bone.matrix) for bone in rig.pose.bones]))
    finally:
        evaluation.restore()
    return np.array(samples), [scene.frame_start, scene.frame_end], scene.render.fps / scene.render.fps_base


def main():
    name = sys.argv[sys.argv.index('--') + 1]
    candidates = ROOT / '.cache/house/candidates'
    source = candidates / 'sources' / (name + '.blend')
    exported = candidates / (name + '.glb')
    report = json.loads((ROOT / '.cache/house/validated' / (name + '.json')).read_text())
    runtime = json.loads((ROOT / '.cache/house/runtime' / (name + '.json')).read_text())
    assert report['passed'] and runtime['passed'], name
    assert digest(source) == report['sourceSha256'] == runtime['sourceSha256']
    assert digest(exported) == report['exportSha256'] == runtime['exportSha256']
    bpy.ops.wm.open_mainfile(filepath=str(source))
    dance_tools.register()
    signature = retrieve_signature(name)
    expected, playback_range, rate = retrieve_playback(name)
    destination = ROOT / 'animations/house_dance/sources' / source.name
    dance_tools.save_source(bpy.data.actions[name], destination)
    bpy.ops.wm.open_mainfile(filepath=str(destination))
    dance_tools.register()
    assert retrieve_signature(name) == signature, name
    actual, saved_range, saved_rate = retrieve_playback(name)
    maximum = float(np.abs(actual - expected).max())
    assert maximum < .0001 and playback_range == saved_range and rate == saved_rate == 24
    assert all(not library.is_missing and Path(bpy.path.abspath(library.filepath)).resolve().is_relative_to(ROOT)
               for library in bpy.data.libraries)
    runtime_destination = destination.parent.parent / exported.name
    shutil.copyfile(exported, runtime_destination)
    assert digest(runtime_destination) == report['exportSha256']
    relocation = dict(candidateSourceSha256=report['sourceSha256'], sourceSha256=digest(destination),
                      sourceBytes=destination.stat().st_size, motionSignature=signature,
                      freshRelocatedPlaybackError=maximum, playbackRange=saved_range,
                      sourceFile=destination.relative_to(ROOT).as_posix(),
                      exportFile=runtime_destination.relative_to(ROOT).as_posix(),
                      frames=[0,.1,12.25,24.5,48,72.75,95.9,96])
    output = ROOT / '.cache/house/finalized' / (name + '.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(relocation, indent=2)+'\n')
    print('FINALIZED', name, maximum, flush=True)


if __name__ == '__main__':
    main()
