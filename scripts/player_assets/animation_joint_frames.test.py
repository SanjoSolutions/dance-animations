"""Check that portable joint limits follow a moving arm's anatomical space."""

import math
from pathlib import Path
import sys
import tempfile

import bpy
from mathutils import Euler, Matrix

sys.path.insert(0, str(Path(__file__).resolve().parent))
from animation_joint_frames import AnimationJointFrames


def main():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    armature = bpy.data.armatures.new("Arm")
    rig = bpy.data.objects.new("Man.rigify", armature)
    scene.collection.objects.link(rig)
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    parent = armature.edit_bones.new("ORG-forearm.L")
    parent.head, parent.tail = (0, 0, 0), (0, 1, 0)
    hand = armature.edit_bones.new("hand_tweak.L")
    hand.head, hand.tail, hand.parent = (0, 1, 0), (0, 1.3, 0), parent
    driver = armature.edit_bones.new("MCH-f_index.01_drv.L")
    driver.head, driver.tail, driver.parent = (0, 1.3, 0), (0, 1.4, 0), hand
    finger = armature.edit_bones.new("f_index.01.L")
    finger.head, finger.tail, finger.parent = (0, 1.3, 0), (0, 1.4, 0), driver
    bpy.ops.object.mode_set(mode="OBJECT")
    bone = rig.pose.bones["hand_tweak.L"]
    bone.rotation_mode = "XYZ"
    constraint = bone.constraints.new("LIMIT_ROTATION")
    constraint.name = "Natural Wrist Rotation"
    constraint.owner_space = "CUSTOM"
    constraint.euler_order = "XYZ"
    for axis in "xyz":
        setattr(constraint, "use_limit_" + axis, True)
        setattr(constraint, "min_" + axis, -0.5)
        setattr(constraint, "max_" + axis, 0.5)
    finger = rig.pose.bones["f_index.01.L"]
    finger.rotation_mode = "XYZ"
    finger_constraint = finger.constraints.new("LIMIT_ROTATION")
    finger_constraint.name = "Natural Finger Rotation"
    finger_constraint.owner_space = "CUSTOM"
    finger_constraint.euler_order = "XYZ"
    for axis in "xyz":
        setattr(finger_constraint, "use_limit_" + axis, True)
        setattr(finger_constraint, "min_" + axis, -0.5)
        setattr(finger_constraint, "max_" + axis, 0.5)

    AnimationJointFrames(scene).restore()
    frame = constraint.space_object
    assert frame and frame.parent == rig
    AnimationJointFrames(scene).restore()
    assert constraint.space_object == frame
    assert len(scene.objects) == 3
    rig.pose.bones["ORG-forearm.L"].rotation_mode = "XYZ"
    rig.pose.bones["ORG-forearm.L"].rotation_euler.z = math.pi / 2
    bone.rotation_euler.x = 0.2
    finger.rotation_euler.x = 0.3
    bpy.context.view_layer.update()
    expected = (rig.pose.bones["ORG-forearm.L"].matrix
                @ Matrix.Translation((0, 1, 0))
                @ Euler((0.2, 0, 0)).to_matrix().to_4x4())
    assert bone.matrix.to_quaternion().rotation_difference(expected.to_quaternion()).angle < 0.0001
    finger_expected = (expected @ Matrix.Translation((0, 0.3, 0))
                       @ Euler((0.3, 0, 0)).to_matrix().to_4x4())
    assert finger.matrix.to_quaternion().rotation_difference(finger_expected.to_quaternion()).angle < 0.0001

    with tempfile.TemporaryDirectory(prefix="dance-joint-frames-") as directory:
        source = Path(directory) / "arm.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(source))
        bpy.ops.wm.open_mainfile(filepath=str(source))
        rig = bpy.context.scene.objects["Man.rigify"]
        bone = rig.pose.bones["hand_tweak.L"]
        assert bone.constraints[0].space_object.parent == rig
        assert bone.matrix.to_quaternion().rotation_difference(expected.to_quaternion()).angle < 0.0001
        finger = rig.pose.bones["f_index.01.L"]
        assert finger.matrix.to_quaternion().rotation_difference(finger_expected.to_quaternion()).angle < 0.0001
    print("Anatomical wrist space follows the arm and survives save/reopen.", flush=True)


if __name__ == "__main__":
    main()
