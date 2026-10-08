"""Bake one saved House candidate through the bundled native deformation bakery."""
import hashlib
import json
from pathlib import Path
import sys

import bpy

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from bake_timing import BakeTiming
import dance_tools
from track_chooser import TrackChooser
from import_assets import read_glb


def main():
    name = sys.argv[sys.argv.index('--') + 1]
    directory = ROOT / '.cache/house/candidates'
    source = directory / 'sources' / (name + '.blend')
    bpy.ops.wm.open_mainfile(filepath=str(source))
    dance_tools.register()
    TrackChooser(bpy.context.scene).apply(name)
    action = bpy.data.actions[name]
    with BakeTiming(action):
        destination = dance_tools.export_action(action, directory / (name + '.glb'), update_catalog=False)
    baked = bpy.data.actions[name + '.baked']
    baked['animation_loop_end_exclusive'] = action.get('animation_loop_end_exclusive', False)
    TrackChooser(bpy.context.scene).apply(name)
    dance_tools.save_source(action, source)
    document, _ = read_glb(destination)
    report = dict(id=name, sourceSha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  exportSha256=hashlib.sha256(destination.read_bytes()).hexdigest(),
                  animationName=document['animations'][0]['name'],
                  duration=max(document['accessors'][sampler['input']]['max'][0]
                               for sampler in document['animations'][0]['samplers']),
                  sourceBytes=source.stat().st_size, exportBytes=destination.stat().st_size,
                  blender=bpy.app.version_string, sampleRate=48)
    output = ROOT / '.cache/house/exported' / (name + '.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + '\n')
    print('EXPORTED', json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
