"""Normalize mesh bind transforms and export standard MPFB models from the studio."""
from pathlib import Path
import bpy
from mathutils import Matrix

ROOT = Path(__file__).resolve().parents[1]


def normalize_meshes():
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH' and obj.name.startswith(('Man.', 'Woman.')) and not obj.get('dance_wardrobe_asset'):
            if obj.name == 'Woman.body':
                height = max(vertex.co.z for vertex in obj.data.vertices) - min(vertex.co.z for vertex in obj.data.vertices)
                if height < .5:
                    obj.data.transform(Matrix.Scale(10, 4))
                if abs(obj.scale.z - .1) < 1e-5:
                    obj.scale = (1, 1, 1)
            obj.hide_set(False)
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)


def main():
    from character_library import CharacterLibrary
    template = ROOT / 'animations/shared_scene_data.blend'
    for path in (ROOT / 'main.blend', template):
        bpy.ops.wm.open_mainfile(filepath=str(path))
        CharacterLibrary.localize()
        normalize_meshes()
        CharacterLibrary().link()
        bpy.ops.wm.save_as_mainfile(filepath=str(path), compress=True)
    for actor in ('Man', 'Woman'):
        from wardrobe import apply_profile
        apply_profile(None)
        bpy.ops.object.select_all(action='DESELECT')
        rig = bpy.context.scene.objects[actor + '.rigify_deform']
        for bone in rig.pose.bones:
            for constraint in bone.constraints:
                constraint.mute = True
            bone.matrix_basis.identity()
        rig.data.pose_position = 'REST'
        rig.select_set(True)
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH' and obj.name.startswith(actor + '.') and not obj.get('dance_wardrobe_asset'):
                obj.hide_set(False)
                obj.select_set(True)
        bpy.context.view_layer.objects.active = rig
        bpy.ops.export_scene.gltf(filepath=str(ROOT / 'models' / ('mpfb-' + actor.lower() + '.glb')),
            export_format='GLB', use_selection=True, export_animations=False, export_skins=True,
            export_def_bones=True, export_morph=False, export_apply=True, export_extras=False,
            export_cameras=False, export_lights=False)
        rig.data.pose_position = 'POSE'
        for bone in rig.pose.bones:
            for constraint in bone.constraints:
                constraint.mute = False
    print('Normalized MPFB bind transforms and exported models.', flush=True)


if __name__ == '__main__':
    main()
