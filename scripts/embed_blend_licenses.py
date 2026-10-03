"""Keep asset credits and embedded-code licenses with the Blender artifacts."""
import json
import sys
from pathlib import Path
import bpy

ROOT = Path(__file__).resolve().parents[1]


def add_text(name, content):
    text = bpy.data.texts.get(name) or bpy.data.texts.new(name)
    text.clear()
    text.write(content)
    text.use_fake_user = True
    return text


def main():
    records = json.loads((ROOT / 'assets/mpfb/attribution.json').read_text())
    manifest = json.loads((ROOT / 'assets/wardrobe/libraries.json').read_text())
    garments = {} if '--studios-only' in sys.argv else manifest
    for identifier, entry in garments.items():
        bpy.ops.wm.read_factory_settings(use_empty=True)
        path = ROOT / entry['file']
        with bpy.data.libraries.load(str(path), link=False) as (available, loaded):
            loaded.collections = available.collections
        record = dict(asset=identifier, **records['clothes/' + identifier])
        for collection in loaded.collections:
            for obj in collection.objects:
                obj.data['dance_asset_credit'] = json.dumps(record)
        notice = add_text('ASSET_LICENSE.txt', json.dumps(record, indent=2) + '\n')
        bpy.data.libraries.write(str(path), {*loaded.collections, notice}, path_remap='RELATIVE_ALL', compress=True)
    notice = (ROOT / 'THIRD_PARTY_NOTICES.md').read_text() + '\n\n' + (ROOT / 'public/third-party/asset-notices.txt').read_text()
    for path in (ROOT / 'assets/characters/mpfb-characters.blend', ROOT / 'animations/shared_scene_data.blend', ROOT / 'main.blend'):
        bpy.ops.wm.open_mainfile(filepath=str(path))
        add_text('LICENSE.txt', (ROOT / 'LICENSE').read_text())
        add_text('THIRD_PARTY_NOTICES.txt', notice)
        add_text('GPL-2.0.txt', (ROOT / 'public/third-party/GPL-2.0.txt').read_text())
        add_text('GPL-3.0.txt', (ROOT / 'public/third-party/GPL-3.0.txt').read_text())
        bpy.ops.wm.save_as_mainfile(filepath=str(path), compress=True)
    print('Embedded original asset credits and applicable code licenses in Blender artifacts.', flush=True)


if __name__ == '__main__':
    main()
