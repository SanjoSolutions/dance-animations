"""Verify editable MPFB targets, portable body links, and the dance rigs."""
import importlib
from pathlib import Path
import shutil
import sys
import tempfile
import bpy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from character_library import CharacterLibrary
from rig_schema import retrieve_bones


def check_rigs():
    schema = retrieve_bones()
    for rig in bpy.context.scene.objects:
        if rig.type == 'ARMATURE' and rig.name in schema:
            assert set(rig.data.bones.keys()) == set(schema[rig.name])


def main():
    library = CharacterLibrary()
    for path in (ROOT / 'main.blend', ROOT / 'animations/shared_scene_data.blend'):
        bpy.ops.wm.open_mainfile(filepath=str(path))
        assert path.stat().st_size < 100_000_000
        for actor in ('Man', 'Woman'):
            body = bpy.data.objects[actor + '.body']
            assert body.data.library and body.data.library.filepath.startswith('//')
            assert Path(bpy.path.abspath(body.data.library.filepath)).resolve() == library.path
            assert len(body.data.shape_keys.key_blocks) > 8
        check_rigs()
    with tempfile.TemporaryDirectory(dir=ROOT / '.cache', prefix='mpfb-edit-') as temporary:
        root = Path(temporary)
        shutil.copytree(ROOT / 'assets', root / 'assets')
        bpy.ops.wm.open_mainfile(filepath=str(root / 'assets/characters/mpfb-characters.blend'))
        check_rigs()
        services = importlib.import_module('bl_ext.blender_org.mpfb.services')
        properties = importlib.import_module('bl_ext.blender_org.mpfb.entities.objectproperties').HumanObjectProperties
        for actor in ('Man', 'Woman'):
            body = bpy.data.objects[actor + '.body']
            assert body.data.library is None and body.data.shape_keys.is_editable
            assert services.ObjectService.get_object_type(body) == 'Basemesh'
            weights = [key.value for key in body.data.shape_keys.key_blocks]
            properties.set_value('weight', .65, entity_reference=body)
            services.TargetService.reapply_macro_details(body)
            assert weights != [key.value for key in body.data.shape_keys.key_blocks]
            assert abs(services.TargetService.get_macro_info_dict_from_basemesh(body)['weight'] - .65) < 1e-5
        destination = root / 'assets/characters/mpfb-characters.blend'
        bpy.ops.wm.save_as_mainfile(filepath=str(destination), compress=True)
        bpy.ops.wm.open_mainfile(filepath=str(destination))
        for actor in ('Man', 'Woman'):
            assert abs(services.TargetService.get_macro_info_dict_from_basemesh(bpy.data.objects[actor + '.body'])['weight'] - .65) < 1e-5
        studio = root / 'main.blend'
        shutil.copyfile(ROOT / 'main.blend', studio)
        bpy.ops.wm.open_mainfile(filepath=str(studio))
        for actor in ('Man', 'Woman'):
            body = bpy.data.objects[actor + '.body']
            assert Path(bpy.path.abspath(body.data.library.filepath)).resolve() == destination
            assert body.data.shape_keys.key_blocks
    print('MPFB macro editing, saved targets, linked characters, portable paths, and dance rigs passed.', flush=True)


if __name__ == '__main__':
    main()
