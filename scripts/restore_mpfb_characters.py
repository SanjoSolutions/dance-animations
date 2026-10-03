"""Restore MPFB target stacks from a-game and link the editable character library.

Run with MPFB enabled: blender --background --python scripts/restore_mpfb_characters.py
Pass -- /path/to/a-game/man_and_woman3.blend to select the original authoring source.
"""
from array import array
import importlib
from pathlib import Path
import sys
import bpy
from mathutils import Matrix

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from character_library import CharacterLibrary
from rig_schema import retain_dance_bones


def restore_targets(source):
    properties = importlib.import_module('bl_ext.blender_org.mpfb.entities.objectproperties').GeneralObjectProperties
    for actor in ('Man', 'Woman'):
        body = bpy.data.objects[actor + '.body']
        current = [vertex.co.copy() for vertex in body.data.vertices]
        with bpy.data.libraries.load(str(source), link=False) as (available, loaded):
            loaded.objects = [actor + '.body']
        original = loaded.objects[0]
        if len(original.data.vertices) != len(body.data.vertices):
            raise ValueError('Preserve the standard hm08 topology for ' + actor)
        # The dance studio normalizes the inherited Woman object scale. Choose
        # the target-stack scale that reproduces the fitted studio geometry.
        original_basis = original.data.shape_keys.reference_key
        original_positions = [point.co.copy() for point in original_basis.data]
        for key in original.data.shape_keys.key_blocks:
            if key != original_basis and key.value:
                for index, point in enumerate(key.data):
                    original_positions[index] += (point.co - original_basis.data[index].co) * key.value
        factors = (1.0, original.scale.x)
        factor = min(factors, key=lambda candidate: max((first - second * candidate).length
                     for first, second in zip(current, original_positions)))
        transform = Matrix.Scale(factor, 4)
        body.data = body.data.copy()
        for original_key in original.data.shape_keys.key_blocks:
            if not original_key.name.startswith('playground_'):
                key = body.shape_key_add(name=original_key.name, from_mix=False)
                coordinates = array('f', (value for point in original_key.data for value in transform @ point.co))
                key.data.foreach_set('co', coordinates)
                key.value = original_key.value
                key.slider_min = original_key.slider_min
                key.slider_max = original_key.slider_max
        basis = body.data.shape_keys.reference_key
        body.data.vertices.foreach_set('co', array('f', (value for point in basis.data for value in point.co)))
        keys = body.data.shape_keys.key_blocks
        restored = [point.co.copy() for point in basis.data]
        for key in keys:
            if key != basis and key.value:
                for index, point in enumerate(key.data):
                    restored[index] += (point.co - basis.data[index].co) * key.value
        difference = max((first - second).length for first, second in zip(current, restored))
        if difference > .00001:
            raise ValueError(f'Preserve the fitted {actor} body: difference {difference}')
        scale = properties.get_value('scale_factor', entity_reference=original)
        properties.set_value('scale_factor', scale * factor, entity_reference=body)
        print('Restored MPFB targets:', actor, len(keys), 'maximum difference', difference, flush=True)
        bpy.data.objects.remove(original, do_unlink=True)
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)


def main():
    source = Path(sys.argv[sys.argv.index('--') + 1]) if '--' in sys.argv else ROOT.parent / 'sanjo-solutions/apps/a-game/man_and_woman3.blend'
    template = ROOT / 'animations/shared_scene_data.blend'
    library = CharacterLibrary()
    bpy.ops.wm.open_mainfile(filepath=str(template))
    restore_targets(source)
    retain_dance_bones()
    library.write()
    # Reopening preserves the studio's relative paths after saving the library copy.
    for path in (template, ROOT / 'main.blend'):
        bpy.ops.wm.open_mainfile(filepath=str(path))
        retain_dance_bones()
        library.link()
        bpy.ops.wm.save_as_mainfile(filepath=str(path), compress=True)
        print('Linked MPFB targets:', path.name, path.stat().st_size, flush=True)


if __name__ == '__main__':
    main()
