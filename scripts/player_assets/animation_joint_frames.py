"""Restore the anatomical spaces used by portable Rigify joint limits."""

import bpy
from mathutils import Matrix


class AnimationJointFrames:
    def __init__(self, scene):
        self.scene = scene

    def restore(self):
        for actor in ("Man", "Woman"):
            rig = self.scene.objects.get(actor + ".rigify")
            if rig and rig.is_editable:
                for bone in rig.pose.bones:
                    for constraint in bone.constraints:
                        if (constraint.type == "LIMIT_ROTATION"
                                and constraint.owner_space == "CUSTOM"
                                and constraint.space_object is None):
                            parent = self.retrieve_parent(rig, bone, constraint.name)
                            if parent:
                                constraint.space_object = self.create_frame(rig, bone, parent)
        bpy.context.view_layer.update()

    @staticmethod
    def retrieve_parent(rig, bone, name):
        if name == "Natural Wrist Rotation":
            return rig.data.bones.get("ORG-forearm." + bone.name.rsplit(".", 1)[-1])
        elif name == "Natural Finger Rotation":
            finger, segment, side = bone.name.split(".")
            return (rig.data.bones[f"{finger}.{int(segment) - 1:02}.{side}"]
                    if int(segment) > 1 else bone.bone.parent.parent)
        else:
            return None

    def create_frame(self, rig, bone, parent):
        name = f"{rig.name}.JointFrame.{bone.name}-noimp"
        frame = self.scene.objects.get(name)
        if frame is None:
            frame = bpy.data.objects.new(name, None)
            self.scene.collection.objects.link(frame)
            frame.is_runtime_data = self.scene.is_runtime_data
            frame.hide_render = True
            frame.hide_set(True)
            frame.hide_select = True
            frame.parent = rig
            frame.parent_type = "BONE"
            frame.parent_bone = parent.name
            rest = parent.matrix_local.inverted() @ bone.bone.matrix_local
            frame.matrix_parent_inverse = Matrix.Identity(4)
            frame.matrix_basis = Matrix.Translation((0, -parent.length, 0)) @ rest
        return frame
