"""Exercise the portable studio and native authoring workflow with Blender 5.2."""
from pathlib import Path
import sys

import bpy

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import dance_tools
from track_chooser import TrackChooser
from animation_participants import retrieve_active_action
from animation_editing import AnimationTrackEditor
from animation_creation import AnimationCreator
from link_wardrobe import ClothingLibraries
from interactable_positioning import POSITIONING


def check_project_libraries():
    assert all(Path(bpy.path.abspath(library.filepath)).resolve().is_relative_to(ROOT)
               for library in bpy.data.libraries)
    garments = ClothingLibraries.retrieve_garments()
    assert garments and all(obj.is_editable and obj.data.library for obj in garments)


def main():
    bpy.ops.wm.open_mainfile(filepath=str(ROOT / 'main.blend'))
    dance_tools.register()
    options = bpy.types.Object.bl_rna.properties['interactable_anatomy_part'].enum_items
    assert set(options.keys()) == {'AUTO', 'HAND_L', 'HAND_R'}
    for actor in ('Man', 'Woman'):
        rig = bpy.context.scene.objects[actor + '.rigify']
        for part in ('HAND_L', 'HAND_R'):
            rig.interactable_anatomy_part = part
            binding = POSITIONING.resolve_binding(rig, bpy.context.scene)
            assert binding and binding.part == part
        rig.interactable_anatomy_part = 'AUTO'
    chooser = TrackChooser(bpy.context.scene)
    assert len(chooser.retrieve_choices()) >= 3512
    chooser.apply('salsa_basic')
    assert bpy.context.scene['dance_wardrobe_profile'] == 'latin'
    assert 'salsa_basic' in chooser.retrieve_tracks()
    assert len(bpy.data.actions) < 20
    check_project_libraries()

    source = ROOT / 'animations/hip_hop/sources/hip_hop_man_bart_simpson.blend'
    bpy.ops.wm.open_mainfile(filepath=str(source))
    dance_tools.register()
    chooser = TrackChooser(bpy.context.scene)
    chooser.apply('hip_hop_man_bart_simpson')
    assert bpy.context.scene['dance_wardrobe_profile'] == 'street'
    assert any(obj.get('dance_wardrobe_asset') == 'male_casualsuit06' and not obj.hide_render
               for obj in bpy.context.scene.objects)
    AnimationTrackEditor(bpy.context).edit('hip_hop_man_bart_simpson')
    action = retrieve_active_action(bpy.context)
    assert action and action.is_editable
    assert any(slot.identifier == 'OBMan.rigify' for slot in action.slots)
    assert bpy.context.scene.objects['Man.body'].data.vertices

    bpy.context.scene.frame_set(12)
    rig = bpy.context.scene.objects['Man.rigify_deform']
    before = {bone.name: bone.matrix.copy() for bone in rig.pose.bones}
    output = ROOT / '.cache/native-export/hip_hop_man_bart_simpson.glb'
    dance_tools.export_action(action, output, update_catalog=False)
    assert output.is_file()
    saved_source = output.parent / 'sources/hip_hop_man_bart_simpson.blend'
    bpy.ops.wm.open_mainfile(filepath=str(saved_source))
    dance_tools.register()
    bpy.context.scene.frame_set(12)
    rig = bpy.context.scene.objects['Man.rigify_deform']
    maximum = max(abs(original - actual) for bone in rig.pose.bones
                  for original_row, actual_row in zip(before[bone.name], bone.matrix)
                  for original, actual in zip(original_row, actual_row))
    assert maximum < 1e-4, maximum
    check_project_libraries()

    AnimationCreator(bpy.context).create('freestyle_review', {'PLAYER'}, {})
    created = retrieve_active_action(bpy.context)
    assert created.name == 'freestyle_review'
    dance_tools.save_source(created, ROOT / '.cache/native-new-source.blend')
    print('Native studio and authoring workflow passed; maximum bone difference:', maximum, flush=True)


if __name__ == '__main__':
    main()
