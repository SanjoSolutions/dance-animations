"""Choose solo and shared NLA tracks across the scene's animation owners."""

import math
import json
from pathlib import Path
import sys

import bpy


directory = str(Path(__file__).parent / "player_assets")
if directory not in sys.path:
    sys.path.insert(0, directory)


# Blender's label API exposes text; bold glyphs style the displayed name only.
BOLD_LABEL_CHARACTERS = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
    "".join(chr(start + index) for start, length in ((0x1D5D4, 26), (0x1D5EE, 26), (0x1D7EC, 10))
            for index in range(length)),
)


class TrackChooser:
    def __init__(self, scene):
        self.scene = scene
        if 'animation_default_frame_rate' not in scene:
            scene['animation_default_frame_rate'] = [scene.render.fps, scene.render.fps_base]

    def retrieve_owners(self):
        owners = list(self.scene.objects)
        owners.extend({obj.data.shape_keys for obj in self.scene.objects
                       if obj.type == "MESH" and obj.data.shape_keys})
        return owners

    def retrieve_tracks(self):
        tracks_by_name = {}
        for rig in self.retrieve_owners():
            if rig.animation_data:
                for track in rig.animation_data.nla_tracks:
                    if track.strips:
                        tracks_by_name.setdefault(track.name, []).append((rig, track))
        return {
            name: entries for name, entries in sorted(tracks_by_name.items())
        }

    def retrieve_active_name(self):
        tracks = self.retrieve_tracks()
        selected = self.scene.get("Track Chooser Selection")
        active = [
            name for name, entries in tracks.items()
            if all(self.is_track_active(owner, track) for owner, track in entries)
        ]
        return selected if selected in active else next(iter(active), None)

    @staticmethod
    def is_track_active(owner, track):
        animation = owner.animation_data
        contains_action = bool(animation.action and any(
            strip.action == animation.action for strip in track.strips))
        if animation.use_nla:
            editable = animation.action is None or (animation.use_tweak_mode and contains_action)
            return editable and track.is_solo and not track.mute
        else:
            return contains_action

    def retrieve_choices(self):
        choices = [
            (name, name if len(entries) > 1 else f"{name} ({entries[0][0].name})", "")
            for name, entries in self.retrieve_tracks().items()
        ]
        if self.scene.get('animation_library_lazy'):
            root = Path(__file__).resolve().parents[1]
            loaded = {name for name, label, description in choices}
            for record in json.loads((root / 'source-inventory.json').read_text()):
                if record['id'] not in loaded:
                    choices.append((record['id'], record['id'], 'Load the Blender source into the studio'))
        return sorted(choices)

    def apply(self, name):
        if self.scene.get('animation_library_lazy') and name not in self.retrieve_tracks():
            root = Path(__file__).resolve().parents[1]
            record = next((record for record in json.loads((root / 'source-inventory.json').read_text()) if record['id'] == name), None)
            if record:
                from animation_files import AnimationFileLibrary
                AnimationFileLibrary(root / 'animations').link([root / record['file']])
        entries = self.retrieve_tracks().get(name)
        if entries:
            if self.scene == bpy.context.scene and self.scene.is_nla_tweakmode:
                from animation_editing import finish_tweaking
                finish_tweaking(bpy.context)
            ranges = [self.retrieve_strip_range(strip) for _, track in entries for strip in track.strips]
            selected_owners = {owner for owner, track in entries}
            for owner in self.retrieve_owners():
                if isinstance(owner, bpy.types.Key) and owner.is_editable and owner not in selected_owners:
                    data = owner.animation_data
                    if data and data.action and not data.use_nla and any(
                            strip.action == data.action for track in data.nla_tracks for strip in track.strips):
                        data.action.use_fake_user = True
                        data.action = None
            for rig, selected in entries:
                data = rig.animation_data
                data.use_tweak_mode = False
                data.action = None
                data.use_nla = True
                for track in data.nla_tracks:
                    if track.is_solo:
                        track.is_solo = False
                selected.mute = False
                # Blender updates solo state across the whole stack on assignment.
                selected.is_solo = True
            self.scene.frame_start = math.floor(min(start for start, end in ranges))
            self.scene.frame_end = math.ceil(max(end for start, end in ranges))
            self.scene["Track Chooser Selection"] = name
            from animation_participants import retrieve_actions
            from animation_wrist_constraints import AnimationWristConstraints
            action = retrieve_actions().get(name)
            rate = action.get('animation_frame_rate', self.scene['animation_default_frame_rate']) if action else self.scene['animation_default_frame_rate']
            self.scene.render.fps, self.scene.render.fps_base = int(rate[0]), rate[1]
            AnimationWristConstraints(self.scene).apply(action)
            self.scene.frame_set(self.scene.frame_start)
            if self.scene == bpy.context.scene:
                from animation_camera import AnimationCamera
                AnimationCamera(bpy.context).synchronize(name)
            if self.scene == bpy.context.scene and hasattr(bpy.types.Action, "player_asset_player"):
                from animation_objects import synchronize_preview
                synchronize_preview()
            from wardrobe import apply_animation
            apply_animation(name)
        else:
            raise ValueError("Choose an available armature track")

    @staticmethod
    def retrieve_strip_range(strip):
        if strip.type == "CLIP" and strip.action and strip.action.frame_range[0] == strip.action.frame_range[1]:
            return strip.frame_start, strip.frame_start
        else:
            end = strip.frame_end
            if strip.action and strip.action.get("animation_loop_end_exclusive", False):
                end -= 1
            return strip.frame_start, end


class TRACKCHOOSER_OT_choose(bpy.types.Operator):
    bl_idname = "track_chooser.choose"
    bl_label = "Select animation"
    bl_description = "Choose an animation and edit its authoring strips in Pose Mode"
    bl_options = {"REGISTER", "UNDO"}

    track: bpy.props.StringProperty(name="Track")

    def execute(self, context):
        try:
            TrackChooser(context.scene).apply(self.track)
            from animation_editing import AnimationTrackEditor
            AnimationTrackEditor(context).edit(self.track)
            context.scene.tool_settings.use_keyframe_insert_auto = True
        except ValueError as error:
            self.report({"ERROR"}, str(error))
            return {"CANCELLED"}
        context.view_layer.update()
        from shape_key_focus import synchronize_animation
        synchronize_animation(context)
        return {"FINISHED"}


class TRACKCHOOSER_OT_search(bpy.types.Operator):
    bl_idname = "track_chooser.search"
    bl_label = "Select animation"
    bl_description = "Search animation tracks by name and choose one to edit"
    bl_property = "track"

    # Retain the enum strings for Blender throughout the popup's lifetime.
    _choices = []

    def retrieve_choices(self, context):
        return TRACKCHOOSER_OT_search._choices

    track: bpy.props.EnumProperty(name="Animation", items=retrieve_choices)

    def invoke(self, context, event):
        type(self)._choices = TrackChooser(context.scene).retrieve_choices()
        if self._choices:
            context.window_manager.invoke_search_popup(self)
            return {"FINISHED"}
        else:
            self.report({"INFO"}, "Add an NLA track to an armature")
            return {"CANCELLED"}

    def execute(self, context):
        return bpy.ops.track_chooser.choose("EXEC_DEFAULT", track=self.track)


class TRACKCHOOSER_PT_tracks(bpy.types.Panel):
    bl_label = "Animation"
    bl_idname = "TRACKCHOOSER_PT_tracks"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Helpers"
    bl_order = 2

    def draw(self, context):
        self.layout.operator("track_chooser.search", icon="VIEWZOOM")
        self.layout.operator("animation.create", icon="ADD")
        self.layout.operator("animation.rename", icon="GREASEPENCIL")
        self.layout.operator("animation.copy", icon="DUPLICATE")
        if context.scene.get("animation_file_template") or context.scene.get("animation_file_directory"):
            self.layout.operator("animation.save_source_file", icon="FILE_TICK")
        self.layout.operator("animation.make_ergonomic", icon="CONSTRAINT_BONE")
        name = TrackChooser(context.scene).retrieve_active_name()
        action = None
        if hasattr(bpy.types.Action, "player_asset_player"):
            from animation_participants import retrieve_active_action
            action = retrieve_active_action(context)
            if action and not name:
                name = action.name
        if name:
            self.layout.label(text=name.translate(BOLD_LABEL_CHARACTERS), translate=False)
        if action:
            if action.library:
                self.layout.operator("animation.open_source_file", icon="FILE_BLEND")
            settings = self.layout.column()
            settings.enabled = action.is_editable
            from animation_camera import draw as draw_camera
            draw_camera(settings, context, action)
            settings.prop(action, "animation_wrist_constraint")
            settings.label(text="Participants")
            column = settings.column(align=True)
            column.prop(action, "player_asset_player")
            column.prop(action, "player_asset_partner")
            from animation_mixing import draw as draw_mixing
            draw_mixing(settings, action)
            from animation_objects import retrieve_objects, retrieve_label
            objects = retrieve_objects()
            if objects:
                settings.label(text="Objects")
                column = settings.column(align=True)
                for choice in action.animation_objects:
                    from animation_files import retrieve_choice_object
                    obj = retrieve_choice_object(choice)
                    if obj in objects:
                        column.prop(choice, "included", text=retrieve_label(obj))


CLASSES = (TRACKCHOOSER_OT_choose, TRACKCHOOSER_OT_search, TRACKCHOOSER_PT_tracks)


def retrieve_registered_class(cls):
    identifier = cls.__name__
    if issubclass(cls, bpy.types.Operator):
        namespace, operator = cls.bl_idname.split(".")
        identifier = namespace.upper() + "_OT_" + operator
    return cls.__bases__[0].bl_rna_get_subclass_py(identifier)


def register():
    import animation_files
    animation_files.register()
    import animation_camera
    animation_camera.register()
    import posing
    posing.unregister()
    import shape_key_focus
    shape_key_focus.register()
    import ergonomic_pose
    ergonomic_pose.register()
    import animation_creation
    if bpy.types.Operator.bl_rna_get_subclass_py("ANIMATION_OT_create") is None:
        animation_creation.register()
    import animation_management
    if bpy.types.Operator.bl_rna_get_subclass_py("ANIMATION_OT_rename") is None:
        animation_management.register()
    for cls in CLASSES:
        previous = retrieve_registered_class(cls)
        if previous:
            bpy.utils.unregister_class(previous)
        bpy.utils.register_class(cls)
    posing.register()


def unregister():
    import animation_files
    animation_files.unregister()
    import animation_camera
    animation_camera.unregister()
    import posing
    posing.unregister()
    import ergonomic_pose
    ergonomic_pose.unregister()
    import shape_key_focus
    shape_key_focus.unregister()
    import animation_creation
    animation_creation.unregister()
    import animation_management
    animation_management.unregister()
    for cls in reversed(CLASSES):
        registered = retrieve_registered_class(cls)
        if registered:
            bpy.utils.unregister_class(registered)


if __name__ == "__main__":
    register()
