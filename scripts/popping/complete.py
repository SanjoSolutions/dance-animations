"""Resume a Popping checkpoint through native source saving and deformation baking.

Blender 5.2 --background --factory-startup --python-exit-code 1
--python scripts/popping/complete.py -- popping_woman_pose_ready
"""

import json
import argparse
from pathlib import Path
import sys

import bpy
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(Path(__file__).parent), str(ROOT / 'scripts/motion_recovery')]
from repair import digest, bind_source, retime, retrieve_matrices
import dance_tools
from animation_export_evaluation import AnimationExportEvaluation
from choreography import PoppingVocabulary, PoppingCharacter, PoppingActionWriter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('identifier')
    parser.add_argument('--sampling', type=int, choices=(2, 4, 8), default=2)
    arguments = parser.parse_args(sys.argv[sys.argv.index('--') + 1:])
    identifier = arguments.identifier
    character, move = identifier.removeprefix('popping_').split('_', 1)
    clip = next(clip for clip in PoppingVocabulary().clips if clip['name'] == move)
    directory = ROOT / '.cache/motion-recovery' / identifier
    directory.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(ROOT / 'main.blend'))
    dance_tools.register()
    scene = bpy.context.scene
    scene.render.fps, scene.render.fps_base = 24, 1
    empty = bpy.data.actions.new('Recovery setup')
    bind_source(empty)
    bpy.data.actions.remove(empty)
    rig = scene.objects[character.title() + '.rigify']
    deform = scene.objects[character.title() + '.rigify_deform']
    poser = PoppingCharacter(rig)
    evaluation = AnimationExportEvaluation({rig, deform})
    evaluation.prepare()
    try:
        states = [poser.apply(pose) for pose in clip['poses']]
        action = PoppingActionWriter().create(rig, clip, states, character)
        bind_source(action)
        action['animation_loop_end_exclusive'] = True
        action['Motion Recovery'] = 'Completed a-game Popping recipe; native deformation bake; procedural study'
        retime(action, arguments.sampling)
        frames = np.arange(0, action.frame_end + .01, .5)
        reference = []
        for frame in frames:
            scene.frame_set(int(frame), subframe=frame % 1)
            reference.append(retrieve_matrices([deform]))
        np.savez_compressed(directory / 'authored.npz', frames=frames, matrices=np.array(reference))
        output = dance_tools.export_action(action, directory / (identifier + '.glb'), update_catalog=False)
    finally:
        evaluation.restore()
    source = output.parent / 'sources' / (identifier + '.blend')
    baseline = next((entry for entry in json.loads((ROOT / 'catalog.json').read_text())['animations'] if entry['id'] == identifier), None)
    report = dict(id=identifier, style='popping', baselineSource=digest(ROOT / baseline['sourceFile']) if baseline else None,
                  baselineExport=digest(ROOT / baseline['file']) if baseline else None,
                  sourceSha256=digest(source), exportSha256=digest(output), source=str(source.relative_to(ROOT)), export=str(output.relative_to(ROOT)),
                  originalRate=24, originalRange=[0, 48], rate=24 * arguments.sampling,
                  storedRange=[0, 48 * arguments.sampling], loop=True, rotationRepairs=[],
                  boneNames=[[bone.name for bone in deform.pose.bones]], performers=[character], sampledFrames=frames.tolist(),
                  contactSchedule=clip['contacts'],
                  dependencies={str(path.relative_to(ROOT)): digest(path) for path in
                                (ROOT / 'animations/shared_scene_data.blend', ROOT / 'assets/characters/mpfb-characters.blend', ROOT / 'assets/characters/rig-schema.json')},
                  generatorSha256=digest(__file__), recipeSha256=digest(Path(__file__).parent / 'choreography.py'),
                  posingSha256=digest(Path(__file__).parent / 'native_poses.py'), blender=bpy.app.version_string, stage='candidate exported')
    (directory / 'checkpoint.json').write_text(json.dumps(report, indent=2) + '\n')
    print('CANDIDATE', identifier, flush=True)


if __name__ == '__main__':
    main()
