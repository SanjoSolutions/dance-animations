"""Move a pose control to another bone and key its current-frame location."""

import bpy

from natural_pose import POSING_OT_fix_unnatural_pose


class BoneMove:
    def __init__(self, context):
        self.context = context

    def move(self, source_rig, source_name, target_rig, target_name):
        source = self.retrieve_bone(source_rig, source_name)
        target = self.retrieve_bone(target_rig, target_name)
        if source == target:
            raise ValueError("Choose distinct bones for A and B")
        if not source_rig.is_editable:
            raise ValueError("Choose an editable rig for A")
        if source.bone.use_connect or any(source.lock_location):
            raise ValueError("Choose a control with freely editable location channels for A")
        animation = source_rig.animation_data
        if animation and animation.action and not animation.action.is_editable:
            raise ValueError("Choose an editable authoring action for A")
        if animation and animation.use_nla and animation.action is None and animation.nla_tracks:
            raise ValueError("Use Select animation to open its authoring strips before posing")

        self.context.view_layer.update()
        destination = target_rig.matrix_world @ target.matrix.translation
        matrix = source.matrix.copy()
        matrix.translation = source_rig.matrix_world.inverted() @ destination
        local = source_rig.convert_space(
            pose_bone=source, matrix=matrix, from_space="POSE", to_space="LOCAL")
        previous = source.location.copy()
        try:
            source.location = local.translation
            self.context.view_layer.update()
            position = source_rig.matrix_world @ source.matrix.translation
            if (position - destination).length > 0.0001:
                raise ValueError("A's constraints require a freely movable IK control")
            # Blender maps the current scene frame into the active NLA strip.
            if not source.keyframe_insert("location", group=source.name):
                raise ValueError("Choose an action with editable location channels for A")
        except Exception:
            source.location = previous
            self.context.view_layer.update()
            raise

    @staticmethod
    def retrieve_bone(rig, name):
        if rig and rig.type == "ARMATURE" and name in rig.pose.bones:
            return rig.pose.bones[name]
        else:
            raise ValueError("Choose an armature and bone for both A and B")


class POSING_PG_settings(bpy.types.PropertyGroup):
    def poll_armature(self, obj):
        return obj.type == "ARMATURE" and obj.name in bpy.context.scene.objects

    source_rig: bpy.props.PointerProperty(name="Rig", type=bpy.types.Object, poll=poll_armature)
    source_bone: bpy.props.StringProperty(name="Bone", description="IK control to move and key")
    target_rig: bpy.props.PointerProperty(name="Rig", type=bpy.types.Object, poll=poll_armature)
    target_bone: bpy.props.StringProperty(name="Bone", description="Bone whose origin supplies the destination")


class POSING_OT_use_selected(bpy.types.Operator):
    bl_idname = "posing.use_selected"
    bl_label = "Use selected bone"
    bl_description = "Assign the active pose bone to this field"
    bl_options = {"UNDO"}

    endpoint: bpy.props.EnumProperty(items=[("source", "A", ""), ("target", "B", "")])

    @classmethod
    def poll(cls, context):
        return context.active_pose_bone is not None

    def execute(self, context):
        settings = context.scene.posing_settings
        setattr(settings, self.endpoint + "_rig", context.active_pose_bone.id_data)
        setattr(settings, self.endpoint + "_bone", context.active_pose_bone.name)
        return {"FINISHED"}


class POSING_OT_move_to(bpy.types.Operator):
    bl_idname = "posing.move_to"
    bl_label = "Move to"
    bl_description = "Move A to B's bone origin and key A's location at the current frame"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.mode in {"OBJECT", "POSE"}

    def execute(self, context):
        settings = context.scene.posing_settings
        try:
            BoneMove(context).move(settings.source_rig, settings.source_bone,
                                   settings.target_rig, settings.target_bone)
        except (ValueError, RuntimeError) as error:
            self.report({"ERROR"}, str(error))
            return {"CANCELLED"}
        self.report({"INFO"}, f"Moved and keyed {settings.source_bone} at frame {context.scene.frame_current_final:g}")
        return {"FINISHED"}


class POSING_PT_posing(bpy.types.Panel):
    bl_label = "Posing"
    bl_idname = "POSING_PT_posing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Helpers"
    bl_order = 3

    def draw(self, context):
        settings = context.scene.posing_settings
        row = self.layout.row()
        row.alignment = "RIGHT"
        row.operator("posing.fix_unnatural_pose", icon="CONSTRAINT_BONE")
        self.layout.separator()
        self.layout.label(text="Move bone to target")
        for endpoint, label in (("source", "Bone"), ("target", "Target")):
            box = self.layout.box()
            row = box.row()
            row.label(text=label)
            row.operator("posing.use_selected", text="", icon="EYEDROPPER").endpoint = endpoint
            box.prop(settings, endpoint + "_rig")
            rig = getattr(settings, endpoint + "_rig")
            if rig:
                box.prop_search(settings, endpoint + "_bone", rig.data, "bones")
            else:
                box.prop(settings, endpoint + "_bone")
        row = self.layout.row()
        row.alignment = "RIGHT"
        row.enabled = bool(settings.source_rig and settings.source_bone
                           and settings.target_rig and settings.target_bone)
        row.operator("posing.move_to")


CLASSES = (POSING_PG_settings, POSING_OT_use_selected, POSING_OT_move_to,
           POSING_OT_fix_unnatural_pose, POSING_PT_posing)


def register():
    unregister()
    for cls in CLASSES:
        bpy.utils.register_class(cls)
    bpy.types.Scene.posing_settings = bpy.props.PointerProperty(type=POSING_PG_settings)


def unregister():
    if hasattr(bpy.types.Scene, "posing_settings"):
        del bpy.types.Scene.posing_settings
    for cls in reversed(CLASSES):
        previous = cls.__bases__[0].bl_rna_get_subclass_py(cls.__name__)
        if previous:
            bpy.utils.unregister_class(previous)
