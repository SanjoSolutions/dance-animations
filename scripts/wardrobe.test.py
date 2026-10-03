"""Check portable native outfits, coverage masks, and source-template clothing."""
import json
from pathlib import Path
import sys
import bpy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from wardrobe import apply_profile, apply_animation


def check_outfits():
    hair = bpy.context.scene.objects['Woman.braid01']
    assert hair['dance_hair_style'] == 'braid01' and hair['dance_hair_color'] == '#36241a'
    assert any(modifier.type == 'ARMATURE' and modifier.object.name == 'Woman.rigify_deform'
               for modifier in hair.modifiers)
    head = hair.vertex_groups['DEF-spine.006']
    assert all(abs(head.weight(vertex.index) - 1) < 1e-6 for vertex in hair.data.vertices)
    configuration = json.loads((ROOT / 'wardrobe.json').read_text())
    for name, profile in configuration['profiles'].items():
        apply_profile(name)
        for actor in ('Man', 'Woman'):
            visible = {obj['dance_wardrobe_asset'] for obj in bpy.context.scene.objects
                       if obj.name.startswith(actor + '.') and obj.get('dance_wardrobe_asset') and not obj.hide_render}
            assert visible == set(profile[actor.lower()]), (name, actor, visible)
            body = bpy.context.scene.objects[actor + '.body']
            for modifier in body.modifiers:
                if modifier.name.startswith('Delete.'):
                    identifier = modifier.name.removeprefix('Delete.')
                    assert modifier.show_render == (identifier in visible), (name, actor, modifier.name)
            collection = bpy.data.collections[actor]
            assert bpy.data.collections[actor + '.Wardrobe'] in list(collection.children)
    for style, expected in [('hip_hop_man_bart_simpson', 'street'), ('ballroom_samba_argentine_crosses', 'latin'), ('ballet_woman_plie', 'ballet')]:
        apply_animation(style)
        assert bpy.context.scene['dance_wardrobe_profile'] == expected
    textured_images = [image for image in bpy.data.images if image.users and image.source == 'FILE']
    assert textured_images and all(image.packed_file for image in textured_images)

    # The opaque practice outfits cover the torso while retaining the head and hands.
    body = bpy.context.scene.objects['Woman.body']
    armatures = [modifier for modifier in body.modifiers if modifier.type == 'ARMATURE']
    for modifier in armatures:
        modifier.show_viewport = False
    for profile in ('practice', 'pole'):
        apply_profile(profile)
        bpy.context.view_layer.update()
        mesh = body.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
        assert all(not (1.18 < vertex.co.z < 1.5 and abs(vertex.co.x) < .17)
                   for vertex in mesh.vertices), profile
        assert any(vertex.co.z > 1.7 for vertex in mesh.vertices), profile
        assert any(abs(vertex.co.x) > .55 for vertex in mesh.vertices), profile
    for modifier in armatures:
        modifier.show_viewport = True


for path in [ROOT / 'main.blend', ROOT / 'animations/shared_scene_data.blend']:
    bpy.ops.wm.open_mainfile(filepath=str(path))
    check_outfits()
    print('Portable wardrobe passed:', path.name, flush=True)
