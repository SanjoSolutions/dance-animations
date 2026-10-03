"""Check linked clothing, portable paths, and editable library rebuilding."""
import json
from pathlib import Path
import shutil
import sys
import tempfile

import bpy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from link_wardrobe import ClothingLibraries
from wardrobe import apply_profile


def check_studio(root):
    garments = ClothingLibraries.retrieve_garments()
    assert garments
    for obj in garments:
        actor = obj.name.split('.', 1)[0]
        assert obj.library is None and obj.is_editable
        assert obj.data.library and obj.data.library.filepath.startswith('//')
        library = Path(bpy.path.abspath(obj.data.library.filepath)).resolve()
        assert library.is_relative_to(root / 'assets/wardrobe') and library.is_file()
        assert all(material.library == obj.data.library for material in obj.data.materials)
        assert all(node.image.library == obj.data.library and node.image.packed_file
                   for material in obj.data.materials for node in material.node_tree.nodes
                   if node.type == 'TEX_IMAGE' and node.image)
        modifiers = [modifier for modifier in obj.modifiers if modifier.type == 'ARMATURE']
        assert modifiers and all(modifier.object == bpy.data.objects[actor + '.rigify_deform']
                                 for modifier in modifiers)
    configuration = json.loads((ROOT / 'wardrobe.json').read_text())
    for name, profile in configuration['profiles'].items():
        apply_profile(name)
        for actor in ('Man', 'Woman'):
            visible = {obj['dance_wardrobe_asset'] for obj in garments
                       if obj.name.startswith(actor + '.') and not obj.hide_render}
            assert visible == set(profile[actor.lower()])


def main():
    for path in (ROOT / 'main.blend', ROOT / 'animations/shared_scene_data.blend'):
        assert path.stat().st_size < 100_000_000
        bpy.ops.wm.open_mainfile(filepath=str(path))
        check_studio(ROOT)
    for path in (ROOT / 'assets/wardrobe').glob('*.blend'):
        assert path.stat().st_size < 100_000_000

    with tempfile.TemporaryDirectory(dir=ROOT / '.cache', prefix='linked-wardrobe-') as temporary:
        root = Path(temporary)
        shutil.copytree(ROOT / 'assets/wardrobe', root / 'assets/wardrobe')
        shutil.copytree(ROOT / 'assets/characters', root / 'assets/characters')
        studio = root / 'animations/shared_scene_data.blend'
        studio.parent.mkdir()
        shutil.copyfile(ROOT / 'animations/shared_scene_data.blend', studio)
        bpy.ops.wm.open_mainfile(filepath=str(studio))
        check_studio(root)

        # Rewriting linked libraries retains a new material edit on relinking.
        obj = ClothingLibraries.retrieve_garments()[0]
        material = obj.data.materials[0].copy()
        original = obj.data
        obj.data = original.copy()
        obj.data.materials[0] = material
        if original.users == 0:
            bpy.data.meshes.remove(original)
        material.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value = .31
        name = obj.name
        libraries = ClothingLibraries(root)
        libraries.write()
        libraries.link()
        assert abs(bpy.data.objects[name].data.materials[0].node_tree.nodes[
            'Principled BSDF'].inputs['Roughness'].default_value - .31) < 1e-6
        check_studio(root)
        apply_profile('street')
        bpy.ops.wm.save_as_mainfile(filepath=str(studio), compress=True)
        assert studio.stat().st_size < 100_000_000
        bpy.ops.wm.open_mainfile(filepath=str(studio))
        check_studio(root)

        # Library collections provide fitted meshes for direct asset editing.
        for entry in json.loads(libraries.manifest.read_text()).values():
            bpy.ops.wm.read_factory_settings(use_empty=True)
            with bpy.data.libraries.load(str(root / entry['file']), link=False) as (available, loaded):
                loaded.collections = available.collections
            for collection in loaded.collections:
                bpy.context.scene.collection.children.link(collection)
                assert collection.objects
                assert all(obj.data.is_editable and obj.data.vertices for obj in collection.objects)
                assert all(obj.parent is None for obj in collection.objects)
                assert all(modifier.type != 'ARMATURE' for obj in collection.objects for modifier in obj.modifiers)
            linked = [(owner.name, owner.library.filepath) for owner in bpy.data.user_map() if owner.library]
            assert linked == [], (entry['file'], linked)
    print('Linked clothing, portable studio, and editable library rebuild passed.', flush=True)


if __name__ == '__main__':
    main()
