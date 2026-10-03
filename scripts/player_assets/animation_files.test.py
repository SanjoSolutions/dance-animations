"""Check fresh Blender startup, editing, and reopening both source formats."""
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile

import bpy

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import dance_tools
from animation_participants import retrieve_active_action
from animation_editing import AnimationTrackEditor
from track_chooser import TrackChooser


def check_scene(name):
    scene = bpy.context.scene
    assert scene.is_runtime_data and scene['animation_file_source'] == name
    for actor in ('Man', 'Woman'):
        assert scene.objects[actor + '.body'].data.vertices
        assert scene.objects[actor + '.rigify'].is_editable
    assert TrackChooser(scene).retrieve_active_name() == name
    AnimationTrackEditor(bpy.context).edit(name)
    assert retrieve_active_action(bpy.context).is_editable
    scene.frame_set(12)
    scene.frame_set(scene.frame_start)


def main():
    if '--' in sys.argv:
        name = sys.argv[sys.argv.index('--') + 1]
        check_scene(name)
        with tempfile.TemporaryDirectory(dir=ROOT / '.cache', prefix='source-editor-') as temporary:
            destination = Path(temporary) / (name + '.blend')
            bpy.ops.wm.save_as_mainfile(filepath=str(destination), compress=True)
            bpy.ops.wm.open_mainfile(filepath=str(destination))
            check_scene(name)
        print('Fresh source editor and save/reopen passed:', name, flush=True)
    else:
        for style, name in (('afro_house', 'afro_house_woman_alternating_arm_pump'),
                            ('hip_hop', 'hip_hop_man_bart_simpson'), ('salsa', 'salsa_basic')):
            source = ROOT / 'animations' / style / 'sources' / (name + '.blend')
            original = hashlib.sha256(source.read_bytes()).hexdigest()
            result = subprocess.run([bpy.app.binary_path, '--background', '--factory-startup',
                str(source), '--python-exit-code', '1', '--python', str(ROOT / 'scripts/open_studio.py'),
                '--python', str(Path(__file__).resolve()), '--', name], capture_output=True, text=True)
            print(result.stdout, result.stderr, flush=True)
            assert result.returncode == 0
            assert hashlib.sha256(source.read_bytes()).hexdigest() == original


if __name__ == '__main__':
    main()
