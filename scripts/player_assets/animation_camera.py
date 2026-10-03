"""Optional camera transforms stored in the selected animation's shared action."""

import bpy
from mathutils import Matrix, Vector

from animation_viewport import AnimationViewport


class AnimationCamera:
    CAMERA = "Animation Camera"
    DEFAULT_TRANSFORM = "Animation Camera Default Transform"

    def __init__(self, context):
        self.context = context
        self.scene = context.scene

    def retrieve_camera(self):
        camera = self.scene.get(self.CAMERA)
        return camera if isinstance(camera, bpy.types.Object) and camera.type == "CAMERA" else None

    def ensure(self):
        camera = self.retrieve_camera()
        if camera is None:
            collection = bpy.data.collections.new("Animation Cameras")
            self.scene.collection.children.link(collection)
            camera = bpy.data.objects.new(self.CAMERA, bpy.data.cameras.new(self.CAMERA))
            collection.objects.link(camera)
            camera.location = (3, -5, 2.5)
            camera.rotation_euler = (Vector((0, 0, 1)) - camera.location).to_track_quat("-Z", "Y").to_euler()
            camera.data.lens = 40
            camera.data.display_size = 0.25
            self.context.view_layer.update()
            self.scene[self.CAMERA] = camera
            self.scene[self.DEFAULT_TRANSFORM] = [value for row in camera.matrix_world for value in row]
        if self.scene.camera is None:
            self.scene.camera = camera
        return camera

    def retrieve_track(self, name):
        camera = self.retrieve_camera()
        return camera.animation_data.nla_tracks.get(name) if camera and camera.animation_data else None

    def synchronize(self, name):
        camera = self.retrieve_camera()
        if camera and self.retrieve_track(name) is None:
            animation = camera.animation_data
            if animation:
                animation.action = None
                for track in animation.nla_tracks:
                    track.is_solo = False
                    track.mute = True
            values = self.scene[self.DEFAULT_TRANSFORM]
            camera.matrix_world = Matrix([values[index:index + 4] for index in range(0, 16, 4)])

    def pose(self):
        from animation_editing import AnimationTrackEditor
        from animation_object_editing import AnimationObjectEditor
        from animation_participants import retrieve_active_action
        from track_chooser import TrackChooser
        action = retrieve_active_action(self.context)
        camera = self.ensure()
        chooser = TrackChooser(self.scene)
        frame, subframe = self.scene.frame_current, self.scene.frame_subframe
        start, end = self.scene.frame_start, self.scene.frame_end
        AnimationViewport.suspended += 1
        try:
            AnimationObjectEditor(self.context).ensure_tracks(
                action, camera, action.name, chooser.retrieve_tracks()[action.name])
            chooser.apply(action.name)
            AnimationTrackEditor(self.context).edit(action.name, focus=[camera])
            self.scene.frame_start, self.scene.frame_end = start, end
            self.scene.frame_set(frame, subframe=subframe)
            AnimationViewport(self.context.view_layer).select_for_pose([camera])
            self.scene.camera = camera
            self.scene.tool_settings.use_keyframe_insert_auto = True
        finally:
            AnimationViewport.suspended -= 1

    def key_pose(self):
        camera = self.retrieve_camera()
        camera.keyframe_insert("location")
        rotation = {"QUATERNION": "rotation_quaternion", "AXIS_ANGLE": "rotation_axis_angle"}.get(
            camera.rotation_mode, "rotation_euler")
        camera.keyframe_insert(rotation)

    def remove_pose(self):
        from animation_editing import finish_tweaking
        from animation_participants import retrieve_active_action
        action = retrieve_active_action(self.context)
        camera = self.retrieve_camera()
        track = self.retrieve_track(action.name)
        slots = {strip.action_slot for strip in track.strips if strip.action == action and strip.action_slot}
        frame, subframe = self.scene.frame_current, self.scene.frame_subframe
        start, end = self.scene.frame_start, self.scene.frame_end
        AnimationViewport.suspended += 1
        try:
            finish_tweaking(self.context)
            camera.animation_data.nla_tracks.remove(track)
            for slot in slots:
                action.slots.remove(slot)
            bpy.ops.track_chooser.choose(track=action.name)
            self.scene.frame_start, self.scene.frame_end = start, end
            self.scene.frame_set(frame, subframe=subframe)
        finally:
            AnimationViewport.suspended -= 1


class CameraPoseOperator:
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        from animation_participants import retrieve_active_action
        from track_chooser import TrackChooser
        action = retrieve_active_action(context)
        return bool(action and action.is_editable and action.name in TrackChooser(context.scene).retrieve_tracks())


class ANIMATION_OT_pose_camera(CameraPoseOperator, bpy.types.Operator):
    bl_idname = "animation.pose_camera"
    bl_label = "Pose camera"
    bl_description = "Select the animation camera in Object Mode and create its initial pose when needed"

    def execute(self, context):
        AnimationCamera(context).pose()
        return {"FINISHED"}


class ANIMATION_OT_key_camera_pose(CameraPoseOperator, bpy.types.Operator):
    bl_idname = "animation.key_camera_pose"
    bl_label = "Key camera pose"
    bl_description = "Save camera position and rotation at the current animation frame"

    @classmethod
    def poll(cls, context):
        from animation_participants import retrieve_active_action
        camera = AnimationCamera(context).retrieve_camera()
        return bool(super().poll(context) and camera and camera.animation_data
                    and camera.animation_data.use_tweak_mode
                    and camera.animation_data.action == retrieve_active_action(context))

    def execute(self, context):
        AnimationCamera(context).key_pose()
        return {"FINISHED"}


class ANIMATION_OT_remove_camera_pose(CameraPoseOperator, bpy.types.Operator):
    bl_idname = "animation.remove_camera_pose"
    bl_label = "Remove camera pose"
    bl_description = "Remove this animation's camera track and keys; retain character poses"

    @classmethod
    def poll(cls, context):
        from animation_participants import retrieve_active_action
        action = retrieve_active_action(context)
        return bool(super().poll(context) and AnimationCamera(context).retrieve_track(action.name))

    def execute(self, context):
        AnimationCamera(context).remove_pose()
        return {"FINISHED"}


def draw(layout, context, action):
    camera = AnimationCamera(context)
    layout.label(text="Camera")
    if camera.retrieve_track(action.name):
        layout.operator("animation.pose_camera", icon="CAMERA_DATA")
        layout.operator("animation.key_camera_pose", icon="KEY_HLT")
        layout.operator("animation.remove_camera_pose", icon="X")
    else:
        layout.operator("animation.pose_camera", text="Add camera pose", icon="ADD")


CLASSES = (ANIMATION_OT_pose_camera, ANIMATION_OT_key_camera_pose, ANIMATION_OT_remove_camera_pose)


def register():
    for cls in CLASSES:
        previous = bpy.types.Operator.bl_rna_get_subclass_py(cls.__name__)
        if previous:
            bpy.utils.unregister_class(previous)
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        registered = bpy.types.Operator.bl_rna_get_subclass_py(cls.__name__)
        if registered:
            bpy.utils.unregister_class(registered)
