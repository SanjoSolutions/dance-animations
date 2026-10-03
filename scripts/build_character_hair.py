"""Update the linked MPFB character and Woman runtime outfits with Melissa's hair."""
import json
from pathlib import Path
import sys
import bpy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_wardrobe import AssetLibrary, WardrobeBuilder
from character_hair import CharacterHair
from character_library import CharacterLibrary
from wardrobe import apply_profile


def main():
    configuration = json.loads((ROOT / 'wardrobe.json').read_text())
    library = AssetLibrary(Path.home() / 'Documents/blender/mpfb/data')
    library.records = json.loads((ROOT / 'assets/mpfb/attribution.json').read_text())
    for path in (ROOT / 'animations/shared_scene_data.blend', ROOT / 'main.blend'):
        bpy.ops.wm.open_mainfile(filepath=str(path))
        CharacterLibrary.localize()
        builder = WardrobeBuilder(library, configuration)
        CharacterHair(library, builder.materials, builder.services).apply()
        if path.name == 'shared_scene_data.blend':
            for profile in (None, *configuration['profiles']):
                builder.export(profile, 'Woman')
        apply_profile(configuration['default'])
        characters = CharacterLibrary()
        if path.name == 'shared_scene_data.blend':
            characters.write()
        characters.link()
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=False, do_recursive=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(path), compress=True)
    library.records.pop('hair/bob01', None)
    (ROOT / 'assets/mpfb/attribution.json').write_text(json.dumps(library.records, indent=2) + '\n', newline='\n')
    print('Melissa braid saved in character sources and every Woman outfit.', flush=True)


if __name__ == '__main__':
    main()
