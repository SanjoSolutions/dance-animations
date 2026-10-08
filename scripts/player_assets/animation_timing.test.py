"""Source files retain effective timing across composition and studio selection."""

from pathlib import Path
import sys
import tempfile

import bpy

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import dance_tools
from track_chooser import TrackChooser
from animation_files import AnimationFileLibrary


def main():
    identifier = 'hip_hop_man_bart_simpson'
    source = ROOT / 'animations/hip_hop/sources' / (identifier + '.blend')
    bpy.ops.wm.open_mainfile(filepath=str(source))
    dance_tools.register()
    scene = bpy.context.scene
    scene.render.fps, scene.render.fps_base = 48, 1.001
    with tempfile.TemporaryDirectory(dir=ROOT / '.cache', prefix='timing-') as temporary:
        destination = Path(temporary) / (identifier + '.blend')
        dance_tools.save_source(bpy.data.actions[identifier], destination)
        bpy.ops.wm.open_mainfile(filepath=str(destination))
        dance_tools.register()
        scene = bpy.context.scene
        scene.render.fps = 60
        bpy.ops.wm.save_as_mainfile(filepath=str(destination))
        bpy.ops.wm.open_mainfile(filepath=str(destination))
        dance_tools.register()
        scene = bpy.context.scene
        assert scene.render.fps == 60
        assert abs(scene.render.fps_base - 1.001) < .000001
        AnimationFileLibrary(ROOT / 'animations').link([ROOT / 'animations/salsa/sources/salsa_basic.blend'])
        chooser = TrackChooser(scene)
        salsa_rate = bpy.data.actions['salsa_basic'].get('animation_frame_rate', [24, 1])
        for name, rate, base in ((identifier, 60, 1.001), ('salsa_basic', *salsa_rate), (identifier, 60, 1.001)):
            chooser.apply(name)
            assert scene.render.fps == rate
            assert abs(scene.render.fps_base - base) < .000001
        print('Saved source timing and mixed-rate selection passed', flush=True)


if __name__ == '__main__':
    main()
