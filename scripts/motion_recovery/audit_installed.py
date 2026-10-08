"""Audit portable action descriptors and owner bindings on installed sources."""
import hashlib
import json
from pathlib import Path
import sys

import bpy

ROOT = Path(__file__).resolve().parents[2]


def main():
    entries = {entry['id']: entry for entry in json.loads((ROOT / 'catalog.json').read_text())['animations']}
    for identifier in sys.argv[sys.argv.index('--') + 1:]:
        directory = ROOT / '.cache/motion-recovery' / identifier
        report = json.loads((directory / 'checkpoint.json').read_text())
        entry = entries[identifier]
        source = ROOT / entry['sourceFile']
        assert hashlib.sha256(source.read_bytes()).hexdigest() == entry['sourceSha256']
        bpy.ops.wm.read_factory_settings(use_empty=True)
        with bpy.data.libraries.load(str(source), link=False) as (available, loaded):
            assert identifier + '.baked' in available.actions
            loaded.actions = [identifier]
            loaded.scenes = available.scenes
        action = loaded.actions[0]
        descriptor = next(scene for scene in loaded.scenes if scene.get('animation_file_template'))
        owners = [slot.identifier for slot in action.slots]
        assert sorted(owners) == sorted('OB' + actor.title() + '.rigify' for actor in report['performers'])
        assert list(action.frame_range) == report['storedRange']
        assert descriptor.render.fps / descriptor.render.fps_base == report['rate']
        assert list(action['animation_frame_rate']) == [descriptor.render.fps, descriptor.render.fps_base]
        assert descriptor.frame_end == action.frame_end - int(report['loop'])
        template = (source.parent / descriptor['animation_file_template']).resolve()
        assert template == ROOT / 'animations/shared_scene_data.blend'
        expected = 'BOTH' if len(report['performers']) == 2 else 'PLAYER' if report['performers'] == ['man'] else 'PARTNER'
        assert action['player_asset_participants'] == expected
        result = dict(sourceSha256=entry['sourceSha256'], owners=owners, participants=expected, frameRange=list(action.frame_range),
                      rate=[descriptor.render.fps, descriptor.render.fps_base], playbackEnd=descriptor.frame_end,
                      template=str(template.relative_to(ROOT)), bindings=json.loads(action['animation_file_tracks']), passed=True)
        (directory / 'installed-source.json').write_text(json.dumps(result, indent=2) + '\n')
        print('SOURCE CONTRACT', identifier, flush=True)


if __name__ == '__main__':
    main()
