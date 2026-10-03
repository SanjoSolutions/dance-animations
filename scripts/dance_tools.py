"""Dance authoring, source saving, native deformation baking, and GLB export."""
import json
from pathlib import Path
import sys
import tempfile

import bpy

ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT / 'scripts', ROOT / 'scripts/player_assets', ROOT / 'scripts/blender/extensions'):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))


def save_source(action, destination=None):
    from animation_files import AnimationFileWriter, AnimationTracks, TRACKS_PROPERTY, retrieve_base_name
    from import_assets import style_for
    if action.library:
        raise ValueError('Open the Blender source or copy the animation to edit it')
    family = {item for item in bpy.data.actions if item.library is None and retrieve_base_name(item.name) == action.name}
    action[TRACKS_PROPERTY] = json.dumps(AnimationTracks().retrieve_bindings(family))
    style = style_for(action.name) or 'freestyle'
    destination = Path(destination or ROOT / 'animations' / style / 'sources' / (action.name + '.blend'))
    return AnimationFileWriter().write(action, ROOT / 'animations/shared_scene_data.blend', destination)


def export_action(action, destination=None, update_catalog=True):
    """Bake the native controls, save their source family, and export one clip."""
    from game_rig_tools_version import retrieve_game_rig_tools
    bakery = retrieve_game_rig_tools().GRT_Action_Bakery
    from single_action_bake import SingleActionBake
    from single_animation_export import AnimationClipScene
    from animation_participants import AnimationParticipants, retrieve_selection
    from import_assets import read_glb, export_animation, retrieve_playback_variants, style_for, STYLES
    if action.library:
        raise ValueError('Open the Blender source or copy the animation to export its editable controls')
    rigs = [bpy.context.scene.objects[name + '.rigify_deform'] for name in ('Man', 'Woman')]
    baked_name = SingleActionBake(bakery, rigs).bake(action.name)
    style = style_for(action.name) or 'freestyle'
    destination = Path(destination or ROOT / 'animations' / style / (action.name + '.glb'))
    with tempfile.TemporaryDirectory(prefix='dance-export-') as directory:
        raw = Path(directory) / 'clip.glb'
        with AnimationClipScene(rigs, rigs).activate(baked_name):
            bpy.ops.export_scene.gltf(filepath=str(raw), export_format='GLB', use_selection=True, use_active_scene=True,
                use_visible=False, export_animations=True, export_animation_mode='NLA_TRACKS',
                export_anim_slide_to_zero=True, export_anim_single_armature=False,
                export_force_sampling=True, export_frame_range=False, export_def_bones=False,
                export_optimize_animation_keep_anim_object=True, export_rest_position_armature=True,
                export_armature_object_remove=False, export_apply=False, export_morph=False,
                export_skins=True, export_all_influences=True, export_materials='NONE',
                export_extras=False, export_cameras=False, export_lights=False)
        raw.write_bytes(AnimationParticipants({'man':rigs[0].name,'woman':rigs[1].name}).apply(raw.read_bytes()))
        document, binary = read_glb(raw)
        clip = next(clip for clip in document['animations'] if clip['name'] == baked_name)
        export_animation(raw, document, binary, clip, destination)
    source = save_source(action, destination.parent / 'sources' / (action.name + '.blend'))
    if update_catalog:
        import hashlib
        catalog = json.loads((ROOT / 'catalog.json').read_text())
        previous = next((entry for entry in catalog['animations'] if entry['id'] == action.name), {})
        selection = retrieve_selection(action)
        performers = ['man','woman'] if selection == 'BOTH' else ['man' if selection == 'PLAYER' else 'woman']
        document, binary = read_glb(destination)
        duration = max(document['accessors'][sampler['input']]['max'][0] for sampler in document['animations'][0]['samplers'])
        entry = dict(previous, id=action.name, style=style, label=action.name.replace('_',' ').capitalize(),
            performers=performers, duration=duration, file=destination.relative_to(ROOT).as_posix(),
            sourceFile=source.relative_to(ROOT).as_posix(), sourceSha256=hashlib.sha256(source.read_bytes()).hexdigest(),
            animationName=baked_name, status='Native deformation bake')
        variants = retrieve_playback_variants(entry)
        catalog['animations'] = sorted([item for item in catalog['animations']
            if item['id'] != action.name and item['file'] != entry['file']] + variants,
            key=lambda item:(item['style'],item['id']))
        inventory = json.loads((ROOT / 'source-inventory.json').read_text())
        record = next((item for item in inventory if item['file'] == entry['sourceFile']), None)
        if record is None:
            record = dict(id=action.name, style=style, file=entry['sourceFile'], original=None)
            inventory.append(record)
        record.setdefault('originalSha256', record.get('sha256'))
        record.update(sha256=entry['sourceSha256'], bytes=source.stat().st_size, runtimeExport=entry['file'])
        catalog['sourceCount'] = len(inventory)
        catalog['sourceOnlyCount'] = sum(item['runtimeExport'] is None for item in inventory)
        style_entry = next((item for item in catalog['styles'] if item['id'] == style), None)
        if style_entry is None:
            style_entry = dict(id=style,label=STYLES.get(style,style.capitalize()))
            catalog['styles'].append(style_entry)
        style_entry.update(playable=sum(item['style']==style for item in catalog['animations']), sources=sum(item['style']==style for item in inventory))
        (ROOT / 'catalog.json').write_text(json.dumps(catalog,indent=2)+'\n')
        (ROOT / 'source-inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
    return destination


class DANCE_OT_export(bpy.types.Operator):
    bl_idname = 'dance.export_animation'
    bl_label = 'Bake and export animation GLB'

    def execute(self, context):
        from animation_participants import retrieve_active_action
        try:
            action = retrieve_active_action(context)
            if action is None:
                raise ValueError('Select an authoring animation')
            destination = export_action(action)
            self.report({'INFO'}, 'Saved ' + str(destination.relative_to(ROOT)))
            return {'FINISHED'}
        except Exception as error:
            self.report({'ERROR'}, str(error))
            return {'CANCELLED'}


def draw_export(self, context):
    self.layout.operator('dance.export_animation', icon='EXPORT')


def register():
    from game_rig_tools_version import retrieve_game_rig_tools
    game_rig_tools = retrieve_game_rig_tools()
    bakery, Preferences = game_rig_tools.GRT_Action_Bakery, game_rig_tools.Preferences
    import animation_participants
    import animation_files
    import track_chooser
    import interactable
    if not hasattr(bpy.types.Object, 'interactable'):
        interactable.register()
    if not hasattr(bpy.types.Scene, 'GRT_Action_Bakery'):
        bakery.register()
        addon = bpy.context.preferences.addons.new()
        addon.module = 'game_rig_tools'
        Preferences.register()
    if not hasattr(bpy.types.Action, 'player_asset_player'):
        animation_participants.register()
        track_chooser.register()
        import snap_hand
    if bpy.types.Operator.bl_rna_get_subclass_py('DANCE_OT_export_animation') is None:
        bpy.utils.register_class(DANCE_OT_export)
        track_chooser.TRACKCHOOSER_PT_tracks.append(draw_export)
    animation_files.prepare_animation_file()
    scene = bpy.context.scene
    if len(scene.GRT_Action_Bakery_Rig_Pairs) == 0:
        for actor in ('Man', 'Woman'):
            pair = scene.GRT_Action_Bakery_Rig_Pairs.add()
            pair.Source_Armature = scene.objects.get(actor + '.rigify')
            pair.Target_Armature = scene.objects.get(actor + '.rigify_deform')
            pair.enabled = True
    settings = scene.GRT_Action_Bakery_Global_Settings
    settings.GLOBAL_Baked_Name_Mode = 'SUFFIX'
    settings.GLOBAL_Baked_Name_01 = '.baked'
    settings.BAKE_SETTINGS_Do_Constraint_Clear = False
    settings.BAKE_SETTINGS_Do_Parent_Clear = False
    settings.BAKE_SETTINGS_Do_Object = True
    settings.Bake_Popup = False
    for text in bpy.data.texts:
        if 'rigify_ui' in text.name:
            exec(compile(text.as_string(),text.name,'exec'), {'__name__':'__main__'})
    animation_files.discover_animation_files()
    from wardrobe import apply_animation
    apply_animation(scene.get('Track Chooser Selection', 'hip_hop'))
    print('Dance helpers ready: Helpers > Animation', flush=True)
