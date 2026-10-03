"""Rig-relative authoring envelopes for the project's Rigify characters.

Angles are in radians. These adjustable envelopes describe an animation model;
individual mobility, strength, and muscle activation require a biomechanical model.
"""

import math

import numpy as np


class JointRange:
    def __init__(self, rig, child, parent, ranges, order='XYZ'):
        self.rig = rig
        self.child = rig.pose.bones[child]
        self.parent = rig.pose.bones[parent]
        self.rest = (self.parent.bone.matrix_local.to_quaternion().inverted()
                     @ self.child.bone.matrix_local.to_quaternion())
        self.ranges = np.radians(ranges)
        self.order = order

    def retrieve_error(self):
        relative = (self.rest.inverted() @ self.parent.matrix.to_quaternion().inverted()
                    @ self.child.matrix.to_quaternion())
        angles = np.array(relative.to_euler(self.order))
        return angles - np.clip(angles, self.ranges[:, 0], self.ranges[:, 1])


class BoneSpan:
    """Keep skeletal lengths and joint attachment distances in rest proportions."""

    def __init__(self, rig, name, parent):
        self.rig = rig
        self.bone = rig.pose.bones[name]
        self.parent = rig.pose.bones[parent]
        self.length = self.bone.bone.length
        self.offset = (self.parent.bone.matrix_local.inverted() @ self.bone.bone.head_local)

    def retrieve_error(self):
        scale = self.rig.matrix_world.to_scale()
        attachment = self.bone.head - self.parent.matrix @ self.offset
        length = (self.bone.tail - self.bone.head).length - self.length
        # A small tolerance accommodates Rigify evaluation and authored body proportions.
        values = np.array([*(attachment[i] * scale[i] for i in range(3)), length * max(scale)])
        return values - np.clip(values, -.002, .002)


class PoseAnatomy:
    def __init__(self, rigs):
        self.joints = []
        self.spans = []
        for rig in rigs:
            for side in ('L', 'R'):
                # Elbow and knee bending is measured relative to a straight limb.
                for child, parent, ranges, straight in (
                        ('forearm', 'upper_arm', ((0, 155), (-90, 90), (-8, 8)), True),
                        ('shin', 'thigh', ((-5, 155), (-15, 15), (-8, 8)), True),
                        ('upper_arm', 'shoulder', ((-130, 160), (-100, 100), (-130, 130)), False),
                        ('thigh', 'spine', ((-130, 40), (-55, 55), (-65, 65)), False),
                        ('foot', 'shin', ((-50, 35), (-25, 25), (-30, 30)), False)):
                    child_name = f'ORG-{child}.{side}'
                    parent_name = 'ORG-spine' if parent == 'spine' else f'ORG-{parent}.{side}'
                    if child_name in rig.pose.bones and parent_name in rig.pose.bones:
                        joint = JointRange(rig, child_name, parent_name, ranges)
                        if straight:
                            joint.ranges[0] -= joint.rest.to_euler('XYZ').x
                        self.joints.append(joint)
                        self.spans.append(BoneSpan(rig, child_name, parent_name))
                hand = f'hand_tweak.{side}'
                if hand in rig.pose.bones and f'ORG-forearm.{side}' in rig.pose.bones:
                    # Reuse this file's calibrated wrist axes and animated limits.
                    constraint = rig.pose.bones[hand].constraints.get('Natural Wrist Rotation')
                    ranges = tuple((math.degrees(getattr(constraint, 'min_' + axis)),
                                    math.degrees(getattr(constraint, 'max_' + axis))) for axis in 'xyz') if constraint else (
                                        (-30, 20), (-80, 80), (-80, 70) if side == 'L' else (-70, 80))
                    self.joints.append(JointRange(rig, hand, f'ORG-forearm.{side}', ranges, 'ZXY'))
                    self.spans.append(BoneSpan(rig, hand, f'ORG-forearm.{side}'))
                from finger_joint_limits import FINGERS, FingerJointLimits
                for finger in FINGERS:
                    for segment in (1, 2, 3):
                        name = f'{finger}.{segment:02}.{side}'
                        bone = rig.pose.bones.get(name)
                        if bone and bone.parent and bone.parent.parent:
                            limits = FingerJointLimits(rig, finger, segment, side)
                            self.joints.append(JointRange(rig, name, limits.parent.name,
                                                          np.degrees(limits.ranges)))
                            self.spans.append(BoneSpan(rig, name, limits.parent.name))
            for child, parent, ranges in (
                    ('ORG-spine.006', 'ORG-spine.004', ((-65, 65), (-85, 85), (-45, 45))),
                    ('ORG-spine.004', 'ORG-spine', ((-55, 80), (-50, 50), (-45, 45)))):
                if child in rig.pose.bones and parent in rig.pose.bones:
                    self.joints.append(JointRange(rig, child, parent, ranges))

    def retrieve_residual(self):
        return np.concatenate([joint.retrieve_error() for joint in self.joints]
                              + [span.retrieve_error() * 20 for span in self.spans] + [np.zeros(0)])

    def retrieve_issues(self):
        issues = []
        for joint in self.joints:
            error = max(abs(joint.retrieve_error()))
            if error > math.radians(.5):
                issues.append(f'{joint.rig.name}: {joint.child.name} joint range ({math.degrees(error):.1f} degrees)')
        for span in self.spans:
            if max(abs(span.retrieve_error())) > .001:
                issues.append(f'{span.rig.name}: {span.bone.name} length or attachment')
        return issues
