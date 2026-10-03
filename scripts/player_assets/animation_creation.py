"""Create editable, shared actions from the current character and object pose."""

import bpy

import animation_interactables
import animation_objects
import animation_participants
from animation_viewport import AnimationViewport


class PoseChannels:
    def __init__(self, owner):
        self.owner = owner
        self.values = {}
        self.paths = set()
        if isinstance(owner, bpy.types.Object):
            self._capture_transform(owner)
            if owner.pose:
                for bone in owner.pose.bones:
                    self._capture_transform(bone)
        elif isinstance(owner, bpy.types.Key):
            for key in owner.key_blocks:
                self._capture(key.path_from_id("value"))
        animation = owner.animation_data
        if animation:
            sources = [(animation.action, animation.action_slot)]
            sources.extend((strip.action, strip.action_slot)
                           for track in animation.nla_tracks for strip in track.strips
                           if strip.type == "CLIP")
            for action, slot in sources:
                if action and slot:
                    for layer in action.layers:
                        for strip in layer.strips:
                            bag = strip.channelbag(slot)
                            if bag:
                                for curve in bag.fcurves:
                                    self._capture(curve.data_path)
            for curve in animation.drivers:
                self.values.pop((curve.data_path, curve.array_index), None)

    def _capture_transform(self, target):
        rotation = {"QUATERNION": "rotation_quaternion", "AXIS_ANGLE": "rotation_axis_angle"}.get(
            target.rotation_mode, "rotation_euler")
        properties = ["location", rotation, "scale"]
        if isinstance(target, bpy.types.Object):
            properties.extend(["delta_location", "delta_scale", "delta_rotation_euler",
                               "delta_rotation_quaternion"])
        for name in properties:
            self._capture(target.path_from_id(name))
        for name, value in target.items():
            if isinstance(value, (int, float, bool)) or (
                    hasattr(value, "to_list") and all(isinstance(item, (int, float, bool)) for item in value)):
                self._capture(target.path_from_id() + '["' + bpy.utils.escape_identifier(name) + '"]')

    def _capture(self, path):
        if path not in self.paths:
            self.paths.add(path)
            try:
                value = self.owner.path_resolve(path)
                values = [value] if isinstance(value, (int, float, bool)) else list(value)
                if all(isinstance(component, (int, float, bool)) for component in values):
                    for index, component in enumerate(values):
                        self.values[path, index] = component
            except (ValueError, TypeError, KeyError):
                pass  # Historical tracks can reference properties from an earlier rig layout.

    def create_slot(self, action, strip, frame=0):
        slot = action.slots.new(self.owner.id_type, self.owner.name)
        bag = strip.channelbags.new(slot)
        for (path, index), value in self.values.items():
            curve = bag.fcurves.new(path, index=index)
            curve.keyframe_points.insert(frame, value)
            curve.update_autoflags(self.owner)
        return slot


class AnimationCreator:
    RIGS = {"PLAYER": "Man.rigify", "PARTNER": "Woman.rigify"}

    def __init__(self, context):
        self.context = context

    def create(self, name, participants, objects):
        from track_chooser import TrackChooser
        name = name.strip()
        if not name:
            raise ValueError("Enter an animation name")
        if name in bpy.data.actions or name in TrackChooser(self.context.scene).retrieve_tracks():
            raise ValueError("Choose a distinct animation name")
        roots = []
        for role in [role for role in self.RIGS if role in participants]:
            rig = self.context.scene.objects.get(self.RIGS[role])
            if rig and rig.type == "ARMATURE":
                roots.append(rig)
            else:
                raise ValueError(f"Configure the {role.lower()} authoring rig")
        props = [obj for obj, included in objects.items() if included]
        roots.extend(props)
        if not roots:
            raise ValueError("Select a participant or object")
        owners = list(dict.fromkeys([*roots, *(child for root in props for child in root.children_recursive)]))
        shapes = [obj.data.shape_keys for obj in owners if obj.type == "MESH" and obj.data.shape_keys]
        owners.extend(dict.fromkeys(shapes))
        for owner in owners:
            if not owner.is_editable:
                raise ValueError(f"Use an editable object for {owner.name}")
        with AnimationViewport(self.context.view_layer).reveal(props):
            self.context.view_layer.update()
            snapshots = [PoseChannels(owner) for owner in owners]
        animation_objects.register_properties()
        animation_interactables.register_properties()
        action = bpy.data.actions.new(name)
        action.use_fake_user = True
        layer = action.layers.new("Pose")
        strip = layer.strips.new(type="KEYFRAME")
        slots = [snapshot.create_slot(action, strip) for snapshot in snapshots]
        AnimationViewport.suspended += 1
        try:
            from animation_editing import finish_tweaking
            finish_tweaking(self.context)
            action[animation_participants.PROPERTY] = (
                "BOTH" if len(participants) == 2 else next(iter(participants), "NONE"))
            animation_objects.synchronize_choices(action)
            for choice in action.animation_objects:
                choice.included = objects.get(choice.object, False)
            # New animations start with no Interactables enabled.
            animation_interactables.synchronize_choices(action, self.context.scene)
            if self.context.mode != "OBJECT":
                bpy.ops.object.mode_set(mode="OBJECT")
            for owner, slot in zip(owners, slots):
                animation = owner.animation_data_create()
                animation.use_tweak_mode = False
                if animation.action:
                    animation.action.use_fake_user = True
                animation.action = action
                animation.action_slot = slot
                animation.action_blend_type = "REPLACE"
                animation.action_influence = 1
                animation.use_nla = False
                for track in animation.nla_tracks:
                    track.is_solo = False
                track = animation.nla_tracks.new()
                track.name = action.name
                track.mute = True
                clip = track.strips.new(action.name, 0, action)
                clip.action_slot = slot
                clip.use_sync_length = True
            scene = self.context.scene
            scene["Track Chooser Selection"] = action.name
            from animation_wrist_constraints import AnimationWristConstraints
            AnimationWristConstraints(scene).apply(action)
            scene.frame_start = 0
            scene.frame_end = max(1, scene.frame_end)
            scene.frame_set(0)
            from animation_camera import AnimationCamera
            AnimationCamera(self.context).synchronize(action.name)
            AnimationViewport(self.context.view_layer).apply(participants, objects)
            animation_interactables.apply_selection(action, scene)
            rigs = [obj for obj in owners if isinstance(obj, bpy.types.Object) and obj.type == "ARMATURE"]
            AnimationViewport(self.context.view_layer).select_for_pose([*roots, *rigs])
            scene.tool_settings.use_keyframe_insert_auto = True
        finally:
            AnimationViewport.suspended -= 1
        from shape_key_focus import synchronize_animation
        synchronize_animation(self.context)
        return action

class AnimationCreationObject(bpy.types.PropertyGroup):
    object_name: bpy.props.StringProperty(name="Object")
    included: bpy.props.BoolProperty(name="Included", default=False)


class ANIMATION_OT_create(bpy.types.Operator):
    bl_idname = "animation.create"
    bl_label = "Create animation"
    bl_description = "Create an animation from the current pose with all channels keyed at frame 0"
    bl_options = {"REGISTER", "UNDO"}
    bl_property = "animation_name"

    animation_name: bpy.props.StringProperty(name="Animation name")
    player: bpy.props.BoolProperty(name="Man", default=True)
    partner: bpy.props.BoolProperty(name="Woman", default=True)
    objects: bpy.props.CollectionProperty(type=AnimationCreationObject)

    def invoke(self, context, event):
        action = animation_participants.retrieve_active_action(context)
        self.player = animation_participants.includes(action, "PLAYER")
        self.partner = animation_participants.includes(action, "PARTNER")
        self.objects.clear()
        for obj, included in animation_objects.retrieve_selection(action).items():
            choice = self.objects.add()
            choice.object_name = obj.name
            choice.included = included
        return context.window_manager.invoke_props_dialog(self, width=400, confirm_text="Create")

    def draw(self, context):
        self.layout.prop(self, "animation_name")
        self.layout.label(text="Participants")
        column = self.layout.column(align=True)
        column.prop(self, "player")
        column.prop(self, "partner")
        if self.objects:
            self.layout.label(text="Objects")
            column = self.layout.column(align=True)
            for choice in self.objects:
                obj = context.scene.objects.get(choice.object_name)
                if obj:
                    column.prop(choice, "included", text=animation_objects.retrieve_label(obj))

    def execute(self, context):
        participants = {role for role, enabled in (("PLAYER", self.player), ("PARTNER", self.partner)) if enabled}
        objects = dict.fromkeys(animation_objects.retrieve_objects(), False)
        choices = {choice.object_name: choice.included for choice in self.objects}
        objects.update({obj: choices.get(obj.name, False) for obj in objects})
        try:
            action = AnimationCreator(context).create(self.animation_name, participants, objects)
        except ValueError as error:
            self.report({"ERROR"}, str(error))
            return {"CANCELLED"}
        self.report({"INFO"}, f"Created {action.name}")
        return {"FINISHED"}


CLASSES = (AnimationCreationObject, ANIMATION_OT_create)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
