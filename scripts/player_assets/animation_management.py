"""Rename and copy the actions and NLA tracks belonging to an animation."""

import bpy

from animation_editing import finish_tweaking
from animation_participants import retrieve_active_action
from animation_viewport import AnimationViewport
from track_chooser import TrackChooser


class AnimationSelection:
    def __init__(self, context):
        self.context = context
        chooser = TrackChooser(context.scene)
        tracks = chooser.retrieve_tracks()
        self.name = chooser.retrieve_active_name()
        self.action = retrieve_active_action(context)
        if self.action is None:
            actions = {strip.action for owner, track in tracks.get(self.name, [])
                       for strip in track.strips if strip.action
                       and not strip.action.name.endswith((".baked", "_baked"))}
            if len(actions) == 1:
                self.action = actions.pop()
        if self.action is None:
            raise ValueError("Select an animation with an authoring action")
        self.name = self.name or self.action.name
        self.actions = {self.action: ""}
        for suffix in (".baked", "_baked"):
            action = bpy.data.actions.get(self.action.name + suffix)
            if action:
                self.actions[action] = suffix
        self.names = {action.name: suffix for action, suffix in self.actions.items()}
        self.names[self.name] = ""
        self.tracks = [(owner, track, self.names[name])
                       for name, entries in tracks.items() if name in self.names
                       for owner, track in entries]

    def validate(self, name, copying=False):
        name = name.strip()
        if not name:
            raise ValueError("Enter an animation name")
        if len((name + "_baked").encode("utf-8")) > 63:
            raise ValueError("Choose a shorter animation name")
        targets = {name + suffix for suffix in ("", ".baked", "_baked")}
        action_targets = {name + suffix: action for action, suffix in self.actions.items()}
        for action in bpy.data.actions:
            if action.name in targets and (copying or action_targets.get(action.name) != action):
                raise ValueError("Choose a distinct animation name")
        track_targets = {track: name + suffix for owner, track, suffix in self.tracks}
        for owner in TrackChooser(self.context.scene).retrieve_owners():
            if owner.animation_data:
                for track in owner.animation_data.nla_tracks:
                    if track.name in targets and (copying or track_targets.get(track) != track.name):
                        raise ValueError("Choose a distinct animation name")
        if any(not owner.is_editable for owner, track, suffix in self.tracks):
            raise ValueError("Select an animation with editable tracks")
        if not copying and any(not action.is_editable for action in self.actions):
            raise ValueError("Select an editable animation")
        return name

    def rename(self, name):
        name = self.validate(name)
        AnimationViewport.suspended += 1
        try:
            for action, suffix in self.actions.items():
                action.name = name + suffix
            for owner, track, suffix in self.tracks:
                track.name = name + suffix
                for strip in track.strips:
                    if strip.action in self.actions:
                        strip.name = strip.action.name
            for scene in bpy.data.scenes:
                selected = scene.get("Track Chooser Selection")
                if selected in self.names and (scene == self.context.scene or
                        any(owner in scene.objects.values() for owner, track, suffix in self.tracks
                            if isinstance(owner, bpy.types.Object))):
                    scene["Track Chooser Selection"] = name + self.names[selected]
            self.context.scene["Track Chooser Selection"] = name
        finally:
            AnimationViewport.suspended -= 1
        return self.action

    def copy(self, name):
        name = self.validate(name, copying=True)
        for owner, track, suffix in self.tracks:
            for strip in track.strips:
                if strip.type != "CLIP" or strip.action not in self.actions:
                    raise ValueError("Choose tracks containing this animation's action clips")
                if strip.fcurves or strip.modifiers:
                    raise ValueError("Use action keyframes for animation copying; strip controls require Blender's NLA Duplicate")
        AnimationViewport.suspended += 1
        try:
            finish_tweaking(self.context)
            copies = {}
            for action, suffix in self.actions.items():
                duplicate = action.copy()
                duplicate.name = name + suffix
                duplicate.use_fake_user = True
                copies[action] = duplicate
            for owner, track, suffix in self.tracks:
                duplicate = owner.animation_data.nla_tracks.new()
                duplicate.name = name + suffix
                duplicate.mute = True
                duplicate.lock = track.lock
                for strip in track.strips:
                    self._copy_strip(strip, duplicate, copies[strip.action])
            if not self.tracks:
                self._create_tracks(copies[self.action], name)
            result = bpy.ops.track_chooser.choose(track=name)
            if result != {"FINISHED"}:
                raise ValueError("Select the copied animation with Select animation")
        finally:
            AnimationViewport.suspended -= 1
        return copies[self.action]

    @staticmethod
    def _copy_strip(source, track, action):
        strip = track.strips.new(action.name, int(source.frame_start), action)
        if source.action_slot:
            strip.action_slot = next(slot for slot in action.slots
                                     if slot.identifier == source.action_slot.identifier)
        for property_name in ("action_frame_start", "action_frame_end", "scale", "repeat",
                              "frame_start", "frame_end", "blend_type", "extrapolation",
                              "use_animated_influence", "use_animated_time", "use_animated_time_cyclic", "strip_time",
                              "influence", "blend_in", "blend_out", "use_auto_blend",
                              "use_reverse", "use_sync_length", "mute"):
            setattr(strip, property_name, getattr(source, property_name))

    def _create_tracks(self, action, name):
        for owner in TrackChooser(self.context.scene).retrieve_owners():
            animation = owner.animation_data
            if animation and animation.action == self.action and owner.is_editable:
                track = animation.nla_tracks.new()
                track.name = name
                track.mute = True
                strip = track.strips.new(name, int(action.frame_range[0]), action)
                if animation.action_slot:
                    strip.action_slot = next(slot for slot in action.slots
                                             if slot.identifier == animation.action_slot.identifier)


class AnimationNameDialog:
    bl_options = {"REGISTER", "UNDO"}
    bl_property = "animation_name"

    @classmethod
    def poll(cls, context):
        try:
            AnimationSelection(context)
            return True
        except ValueError:
            return False

    def invoke(self, context, event):
        selection = AnimationSelection(context)
        self.animation_name = selection.name + (" copy" if self.operation == "copy" else "")
        return context.window_manager.invoke_props_dialog(
            self, width=400, confirm_text=self.operation.capitalize())

    def draw(self, context):
        self.layout.prop(self, "animation_name")

    def execute(self, context):
        try:
            action = getattr(AnimationSelection(context), self.operation)(self.animation_name)
        except ValueError as error:
            self.report({"ERROR"}, str(error))
            return {"CANCELLED"}
        for area in context.screen.areas:
            area.tag_redraw()
        self.report({"INFO"}, f"Animation: {action.name}")
        return {"FINISHED"}


class ANIMATION_OT_rename(AnimationNameDialog, bpy.types.Operator):
    bl_idname = "animation.rename"
    bl_label = "Rename animation"
    bl_description = "Rename the current animation and its matching baked actions and tracks"
    operation = "rename"
    animation_name: bpy.props.StringProperty(name="Animation name")


class ANIMATION_OT_copy(AnimationNameDialog, bpy.types.Operator):
    bl_idname = "animation.copy"
    bl_label = "Copy animation"
    bl_description = "Copy the current animation and select the new animation for editing"
    operation = "copy"
    animation_name: bpy.props.StringProperty(name="Animation name")


CLASSES = (ANIMATION_OT_rename, ANIMATION_OT_copy)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
