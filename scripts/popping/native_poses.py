"""Native IK posing adapted from the original a-game disco and yoga authors."""
import math
import bpy
from mathutils import Euler, Matrix, Vector

def retrieve_base_pose():
    return dict(pelvis=(0, 0, 1.00335), bend=0, chest=0, head=0,
                feet=(.12, -.023, .0815), hands=(.23, -.025, .96),
                fingers=(0, 0, -1), palms=(0, -1, 0), elbows=(.5, .5, 1.1),
                knees=(.15, -1, .5), foot_bend=0, feet_turn=0)


class ControlPoser:

    def __init__(self, rig):
        self.rig = rig
        self.controls = [p for p in rig.pose.bones if p.custom_shape]
        self.states = {}

    def update(self):
        self.rig.update_tag()
        bpy.context.view_layer.update()

    def place(self, name, position, rotation):
        matrix = rotation.to_matrix().to_4x4()
        matrix.translation = Vector(position)
        self.rig.pose.bones[name].matrix = matrix

    @staticmethod
    def orientation(direction, normal, sign):
        axis = Vector(direction).normalized()
        normal = Vector(normal)
        normal = (normal - axis * axis.dot(normal)).normalized()
        normal *= sign
        cross = normal.cross(axis).normalized()
        return Matrix((normal, axis, cross)).transposed().to_quaternion()

    def apply(self, pose):
        for bone in self.controls:
            bone.matrix_basis = Matrix.Identity(4)
        for side in ('L', 'R'):
            for prefix in ('thigh_parent.', 'upper_arm_parent.'):
                bone = self.rig.pose.bones[prefix + side]
                bone['IK_FK'] = 0.0
                bone['IK_Stretch'] = 0.0
                bone['pole_vector'] = True
            for prop in ('Surface Contact', 'Finger Contact'):
                self.rig.pose.bones['hand_ik.' + side][prop] = 0.0
            self.rig.pose.bones['hand_ik.' + side]['Contact Target'] = 2
        self.rig.pose.bones['torso']['neck_follow'] = 1.0
        self.rig.pose.bones['torso']['head_follow'] = 1.0
        self.update()
        position = list(pose['pelvis'])
        position[0] += pose.get('pelvis_side', 0)
        self.place('torso', position, Euler(tuple((math.radians(v) for v in (pose['bend'], pose.get('lean', 0), 0))), 'XYZ').to_quaternion())
        self.rig.pose.bones['chest'].rotation_quaternion = Euler((math.radians(pose['chest']), 0, 0)).to_quaternion()
        head = self.rig.pose.bones['head']
        rest = head.bone.matrix_local.to_quaternion()
        head.rotation_quaternion = rest.inverted() @ Euler((math.radians(pose['head']), 0, math.radians(pose.get('head_turn', 0)))).to_quaternion() @ rest
        self.update()
        for side, suffix, sign in (('left', 'L', 1), ('right', 'R', -1)):
            mirror = lambda value: (sign * value[0], value[1], value[2])
            foot = pose.get('foot_targets', {}).get(side, mirror(pose['feet']))
            angles = (pose.get('foot_angles', {}).get(side, pose['foot_bend']), 0, pose.get('foot_turns', {}).get(side, sign * pose['feet_turn']))
            self.place('foot_ik.' + suffix, foot, Euler(tuple((math.radians(v) for v in angles))).to_quaternion())
            hand = pose.get('hand_targets', {}).get(side, mirror(pose['hands']))
            fingers = pose.get('hand_directions', {}).get(side, mirror(pose['fingers']))
            normal = mirror(pose['palms'])
            if abs(Vector(fingers).normalized().dot(Vector(normal).normalized())) > 0.95:
                normal = (0, -1, 0)
            self.place('hand_ik.' + suffix, hand, self.orientation(fingers, normal, sign))
            for prefix, target in (('thigh_ik_target.', pose.get('knee_targets', {}).get(side, mirror(pose['knees']))), ('upper_arm_ik_target.', mirror(pose['elbows']))):
                bone = self.rig.pose.bones[prefix + suffix]
                self.place(bone.name, target, bone.bone.matrix_local.to_quaternion())
        self.update()

    def capture(self, name):
        channels = {}
        for bone in self.controls:
            core = bone.name in {'root', 'torso', 'hips', 'chest', 'head', 'neck', 'jaw_master'}
            body = bone.name.startswith(('spine_', 'tweak_spine', 'shoulder', 'breast', 'palm', 'f_', 'thumb', 'hand_', 'foot_', 'toe_', 'thigh_', 'shin_', 'upper_arm_', 'forearm_'))
            if core or (body and '_fk' not in bone.name):
                rotation = 'rotation_quaternion' if bone.rotation_mode == 'QUATERNION' else 'rotation_euler'
                for prop in ('location', rotation, 'scale'):
                    channels[bone.path_from_id(prop)] = list(getattr(bone, prop))
                for prop, value in bone.items():
                    if isinstance(value, (int, float, bool)):
                        channels[bone.path_from_id() + '["' + bpy.utils.escape_identifier(prop) + '"]'] = [float(value)]
        self.states[name] = channels
        return channels

class DiscoWristPoser:

    def __init__(self, rig):
        self.rig = rig
        self.rest_rotations = {side: rig.data.bones['ORG-forearm.' + side].matrix_local.to_quaternion().inverted() @ rig.data.bones['ORG-hand.' + side].matrix_local.to_quaternion() for side in ('L', 'R')}

    def apply(self, beat):
        phase = math.pi * (beat % 32)
        for side, sign in (('L', 1), ('R', -1)):
            forearm = self.rig.pose.bones['ORG-forearm.' + side]
            hand = self.rig.pose.bones['hand_ik.' + side]
            neutral = forearm.matrix.to_quaternion() @ self.rest_rotations[side]
            accent = Euler(tuple((math.radians(value) for value in (6 * math.sin(phase), sign * 8 * math.sin(phase), sign * 4 * math.cos(phase)))), 'ZXY').to_quaternion()
            matrix = (neutral @ accent).to_matrix().to_4x4()
            matrix.translation = hand.matrix.translation
            hand.matrix = matrix
        self.rig.update_tag()
        bpy.context.view_layer.update()

class DiscoChoreography:

    @staticmethod
    def blend(first, second, amount):
        return tuple((a + (b - a) * amount for a, b in zip(first, second)))

    def retrieve_arms(self, section, beat):
        wave = (1 + math.cos(math.pi * beat)) / 2
        phase = math.pi * beat
        hands = {}
        directions = {}
        for side, sign in (('left', 1), ('right', -1)):
            if section == 0:
                active = (side == 'right') == (beat % 8 < 4)
                if active:
                    hands[side] = self.blend((sign * 0.3, -0.3, 1.04), (sign * 0.43, -0.1, 1.89), wave)
                    directions[side] = (sign * 0.35, -0.1, 2 * wave - 1)
                else:
                    hands[side] = (sign * 0.28, -0.1, 0.98)
                    directions[side] = (0, -0.15, -1)
            elif section == 1:
                reach = (1 + sign * math.cos(phase)) / 2
                hands[side] = self.blend((sign * 0.24, -0.28, 1.2), (sign * 0.57, -0.17, 1.56), reach)
                directions[side] = (sign, -0.3, 0.3)
            elif section == 2:
                angle = phase + (0 if sign == 1 else math.pi)
                hands[side] = (sign * 0.17, -0.35 - 0.07 * math.cos(angle), 1.28 + 0.13 * math.sin(angle))
                directions[side] = (-sign, -0.25, 0.12 * math.cos(angle))
            else:
                reach = (1 + math.cos(phase + sign * math.pi / 2)) / 2
                hands[side] = self.blend((sign * 0.3, -0.13, 1.06), (sign * 0.31, -0.44, 1.4), reach)
                directions[side] = (sign * 0.15, -1, 0.3)
        return (hands, directions)
