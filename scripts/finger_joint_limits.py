"""Native finger joint limits measured from each joint's anatomical parent."""

import math

import bpy
from mathutils import Matrix

from install_contact_order import CHARACTERS, STAGE_COLLECTION


FINGERS = ("f_index", "f_middle", "f_ring", "f_pinky", "thumb")


class FingerJointLimits:
    constraint_name = "Natural Finger Rotation"

    def __init__(self, rig, finger, segment, side):
        self.rig = rig
        self.bone = rig.data.bones[f"{finger}.{segment:02}.{side}"]
        self.parent = (rig.data.bones[f"{finger}.{segment - 1:02}.{side}"] if segment > 1
                       else self.bone.parent.parent)
        self.rest = self.parent.matrix_local.inverted() @ self.bone.matrix_local
        if segment == 1:
            if finger == "thumb":
                opposition = (-85, 15) if side == "L" else (-15, 85)
                ranges = ((-60, 60), opposition, (-45, 45))
            else:
                ranges = ((-25, 90), (0, 0), (-20, 20))
        else:
            rest_bend = math.degrees(self.rest.to_euler("XYZ").x)
            if finger == "thumb":
                extension, flexion = (-10, 70) if segment == 2 else (-20, 90)
            else:
                extension, flexion = (0, 110) if segment == 2 else (-5, 90)
            ranges = ((extension - rest_bend, flexion - rest_bend), (0, 0), (0, 0))
        self.ranges = tuple(tuple(math.radians(angle) for angle in bounds) for bounds in ranges)

    def retrieve_frame(self):
        previous_name = f"{self.rig.name}.JointFrame.{self.bone.name}"
        name = previous_name + "-noimp"
        frame = bpy.data.objects.get(name)
        if frame is None:
            frame = bpy.data.objects.get(previous_name)
            if frame:
                frame.name = name
        if frame is None:
            frame = bpy.data.objects.new(name, None)
            bpy.data.collections[STAGE_COLLECTION].objects.link(frame)
            frame.hide_render = True
            frame.hide_set(True)
            frame.hide_select = True
            frame.parent = self.rig
            frame.parent_type = "BONE"
            frame.parent_bone = self.parent.name
            frame.matrix_parent_inverse = Matrix.Identity(4)
            frame.matrix_basis = Matrix.Translation((0, -self.parent.length, 0)) @ self.rest
        return frame

    def apply(self, owner):
        existing = owner.constraints.get(self.constraint_name)
        if existing:
            owner.constraints.remove(existing)
        constraint = owner.constraints.new("LIMIT_ROTATION")
        constraint.name = self.constraint_name
        constraint.owner_space = "CUSTOM"
        constraint.space_object = self.retrieve_frame()
        constraint.euler_order = "XYZ"
        constraint.use_transform_limit = True
        for axis, (minimum, maximum) in zip("xyz", self.ranges):
            setattr(constraint, f"use_limit_{axis}", True)
            setattr(constraint, f"min_{axis}", minimum)
            setattr(constraint, f"max_{axis}", maximum)


class FingerJointLimitsInstaller:
    def install(self):
        for character in CHARACTERS:
            for suffix in ("rigify", "ContactBase-noimp", "ContactFirst-noimp", "ContactFinal-noimp"):
                rig = bpy.data.objects[f"{character}.{suffix}"]
                for side in ("L", "R"):
                    for segment in (1, 2, 3):
                        for finger in FINGERS:
                            limits = FingerJointLimits(rig, finger, segment, side)
                            limits.apply(rig.pose.bones[limits.bone.name])
