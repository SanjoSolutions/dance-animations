"""Create the portable dance studio and standard MPFB character exports.

Blender 5.2 --background --factory-startup --python-exit-code 1
--python scripts/build_studio.py -- ../sanjo-solutions/apps/a-game
"""
import bpy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from rig_schema import retain_dance_bones


def main():
    source = Path(sys.argv[sys.argv.index('--') + 1]).resolve()
    bpy.ops.wm.open_mainfile(filepath=str(source / 'animations/man_and_woman/shared_scene_data.blend'))
    original = next(scene for scene in bpy.data.scenes if scene.objects.get('Man.rigify'))
    snap_hand_version = original.get('Snap Hand Version',1)
    local_objects = {obj.name:obj for obj in original.objects if obj.library is None}
    for obj in local_objects.values():
        if obj.override_library:
            obj.make_local(clear_liboverride=True)
    for obj in list(bpy.data.objects):
        if obj.library and obj.name in local_objects:
            obj.user_remap(local_objects[obj.name])
    studio = bpy.data.scenes.new('Dance studio')
    studio.render.fps = original.render.fps
    studio.render.fps_base = original.render.fps_base
    bpy.context.window.scene = studio
    rigs = [local_objects[name] for name in ('Man.rigify','Woman.rigify','Man.rigify_deform','Woman.rigify_deform')]
    keep = set(rigs)
    for rig in rigs:
        keep.update(bone.custom_shape for bone in rig.pose.bones if bone.custom_shape)
        if rig.animation_data:
            rig.animation_data.action = None
            for track in list(rig.animation_data.nla_tracks):
                rig.animation_data.nla_tracks.remove(track)
    for actor in ('Man','Woman'):
        meshes = [local_objects[name] for name in (actor+'.body',actor+'.high-poly',actor+'.teeth_base',actor+'.tongue01')]
        meshes.extend(obj for name,obj in local_objects.items() if name.startswith(actor+'.')
                      and any(part in name for part in ('bob01','eyelashes01','eyebrow007')))
        for mesh in meshes:
            mesh.data = mesh.data.copy()
            if mesh.data.shape_keys:
                keys = mesh.data.shape_keys
                positions = [point.co.copy() for point in keys.reference_key.data]
                for key in keys.key_blocks:
                    if key != keys.reference_key and key.value:
                        for index,point in enumerate(key.data):
                            positions[index] += (point.co - key.relative_key.data[index].co) * key.value
                mesh.shape_key_clear()
                for vertex,position in zip(mesh.data.vertices,positions):
                    vertex.co = position
            mesh.animation_data_clear()
            for modifier in list(mesh.modifiers):
                if modifier.type == 'MASK' and modifier.name != 'Hide helpers':
                    mesh.modifiers.remove(modifier)
                elif modifier.type == 'ARMATURE' and modifier.name != 'Armature':
                    mesh.modifiers.remove(modifier)
            material = bpy.data.materials.new(actor+' studio material')
            material.diffuse_color = (.64,.72,.82,1) if actor=='Man' else (.80,.72,.58,1)
            material.use_nodes = True
            shader = material.node_tree.nodes.get('Principled BSDF')
            shader.inputs['Base Color'].default_value = material.diffuse_color
            shader.inputs['Roughness'].default_value = .75
            mesh.data.materials.clear()
            mesh.data.materials.append(material)
            for face in mesh.data.polygons:
                face.material_index = 0
            mesh.hide_viewport = mesh.hide_render = False
            keep.add(mesh)
    # Preserve the studio props used by dance control actions, such as the pole.
    props = [obj for name,obj in local_objects.items() if 'pole' in name.lower()
             and not name.startswith(('Man.','Woman.'))]
    keep.update(props)
    for obj in keep:
        if obj.library:
            obj.make_local()
        studio.collection.objects.link(obj)
    # Normalize body scale before skin export so every mesh shares the rig's bind space.
    bpy.ops.object.select_all(action='DESELECT')
    for obj in keep:
        if obj.type == 'MESH' and obj.name.startswith(('Man.', 'Woman.')):
            if obj.name == 'Woman.body' and abs(obj.scale.z - .1) < 1e-5:
                obj.scale = (1, 1, 1)
            obj.hide_set(False)
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    for rig in rigs:
        rig.data = rig.data.copy()
        rig.hide_viewport = False
        rig.hide_set(False)
    # Retain native rig UI scripts and Snap Hand; the project helper starts explicitly.
    keep_texts = [text for text in bpy.data.texts if 'rigify_ui' in text.name or text.name == 'snap_hand.py']
    for scene in list(bpy.data.scenes):
        if scene != studio:
            bpy.data.scenes.remove(scene)
    for obj in list(bpy.data.objects):
        if obj not in keep:
            bpy.data.objects.remove(obj,do_unlink=True)
    for action in list(bpy.data.actions):
        bpy.data.actions.remove(action)
    for text in list(bpy.data.texts):
        if text not in keep_texts:
            bpy.data.texts.remove(text)
    for collection in list(bpy.data.collections):
        if collection.users == 0:
            bpy.data.collections.remove(collection)
    for obj in keep:
        if obj.data and getattr(obj.data,'library',None):
            obj.data = obj.data.copy()
    for _ in range(3):
        bpy.ops.outliner.orphans_purge(do_local_ids=True,do_linked_ids=True,do_recursive=True)
    retain_dance_bones()
    keep = set(studio.objects)
    for rig in rigs:
        rig.data.pose_position = 'POSE'
    studio['animation_file_directory'] = '//animations'
    studio['dance_project'] = True
    studio['Snap Hand Version'] = snap_hand_version
    studio.world = bpy.data.worlds.new('Dance studio world')
    studio.world.color = (.18,.18,.18)
    studio.tool_settings.use_keyframe_insert_auto = True
    studio.frame_start,studio.frame_end = 0,60
    studio.frame_set(0)
    # Save a self-contained template. Pose defaults and native constraints stay intact.
    template = ROOT/'animations/shared_scene_data.blend'
    studio.pop('animation_file_directory',None)
    bpy.ops.wm.save_as_mainfile(filepath=str(template),compress=True)
    for actor in ('Man','Woman'):
        bpy.ops.object.select_all(action='DESELECT')
        deform = local_objects[actor+'.rigify_deform']
        for bone in deform.pose.bones:
            for constraint in bone.constraints:
                constraint.mute = True
            bone.matrix_basis.identity()
        deform.data.pose_position = 'REST'
        meshes = [obj for obj in keep if obj.type=='MESH' and obj.name.startswith(actor+'.')]
        deform.select_set(True)
        for mesh in meshes:
            mesh.hide_set(False)
            mesh.select_set(True)
        bpy.context.view_layer.objects.active = deform
        bpy.ops.export_scene.gltf(filepath=str(ROOT/'models'/('mpfb-'+actor.lower()+'.glb')),
                                  export_format='GLB',use_selection=True,export_animations=False,
                                  export_skins=True,export_def_bones=True,export_morph=False,
                                  export_apply=True,export_extras=False,export_cameras=False,export_lights=False)
        deform.data.pose_position = 'POSE'
        for bone in deform.pose.bones:
            for constraint in bone.constraints:
                constraint.mute = False
    # Reload the saved template to keep the studio independent of export state.
    bpy.ops.wm.open_mainfile(filepath=str(template))
    bpy.context.scene['animation_file_directory'] = '//animations'
    bpy.context.scene['dance_project'] = True
    bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'main.blend'),compress=True)
    print('Standard MPFB studio and GLB models created.',flush=True)


if __name__ == '__main__':
    main()
