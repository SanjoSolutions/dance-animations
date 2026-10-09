"""Repair native Waacking wrist frames and elbow poles along saved hand paths."""
import json
import math
from pathlib import Path
import sys

import bpy
from mathutils import Matrix, Vector

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'scripts/motion_recovery'), str(Path(__file__).parent)]
from repair import main, retrieve_curves
from sole_repair import PlantedSoleRepair


class WaackingArmRepair:
    """Use the elbow bend plane as the forearm and wrist roll reference."""

    def apply(self, action):
        scene = bpy.context.scene
        owner = scene.objects[action.slots[0].identifier[2:]]
        slot = action.slots[0]
        frames = sorted({float(point.co.x) for curve in retrieve_curves(action, slot)
                         if curve.data_path.endswith('location') for point in curve.keyframe_points})
        poles = {side: [] for side in 'LR'}
        for frame in frames:
            scene.frame_set(int(frame), subframe=frame % 1)
            for side, sign in (('L', 1), ('R', -1)):
                bone = owner.pose.bones['upper_arm_ik_target.' + side]
                original = bone.matrix.copy()
                target = original.copy()
                target.translation = owner.pose.bones['ORG-upper_arm.' + side].head + Vector((sign * .35, .8, 0))
                bone.matrix = target
                poles[side].append(tuple(bone.location))
                bone.matrix = original
        for side in 'LR':
            bone = owner.pose.bones['upper_arm_ik_target.' + side]
            for frame, location in zip(frames, poles[side]):
                bone.location = location
                bone.keyframe_insert('location', frame=frame, group=bone.name)
        samples = [index / 2 for index in range(int(action.frame_range[1] * 2) + 1)]
        rotations = {side: [] for side in 'LR'}
        for frame in samples:
            scene.frame_set(int(frame), subframe=frame % 1)
            bpy.context.view_layer.update()
            for side in 'LR':
                forearm = owner.pose.bones['ORG-forearm.' + side]
                hand = owner.pose.bones['hand_ik.' + side]
                original = hand.matrix.copy()
                rest_offset = forearm.bone.matrix_local.to_quaternion().inverted() @ owner.pose.bones['ORG-hand.' + side].bone.matrix_local.to_quaternion()
                rotation = forearm.matrix.to_quaternion() @ rest_offset
                hand.matrix = Matrix.LocRotScale(original.translation, rotation, original.to_scale())
                quaternion = hand.rotation_quaternion.copy().normalized()
                if rotations[side] and quaternion.dot(rotations[side][-1]) < 0:
                    quaternion.negate()
                rotations[side].append(quaternion)
                hand.matrix = original
        counts = {}
        for side in 'LR':
            bone = owner.pose.bones['hand_ik.' + side]
            retained = self.retrieve_keys(samples, rotations[side], math.radians(.15))
            path = bone.path_from_id('rotation_quaternion')
            for layer in action.layers:
                for strip in layer.strips:
                    for bag in strip.channelbags:
                        if bag.slot_handle == slot.handle:
                            for curve in list(bag.fcurves):
                                if curve.data_path == path:
                                    bag.fcurves.remove(curve)
            for index in retained:
                bone.rotation_quaternion = rotations[side][index]
                bone.keyframe_insert('rotation_quaternion', frame=samples[index], group=bone.name)
            for curve in retrieve_curves(action, slot):
                if curve.data_path == path:
                    for point in curve.keyframe_points:
                        point.interpolation = 'LINEAR'
            counts[side] = len(retained)
        action['Waacking Arm Repair'] = json.dumps(dict(elbowPole='shoulder plus outward 0.35 m and posterior 0.8 m',
            wristRoll='evaluated forearm orientation with native rest offset', correctiveKeys=counts,
            fittingStep=.5, angularSimplification=math.radians(.15), trajectory='saved hand, foot, and torso locations'))
        print('ARM_REPAIR', action.name, counts, flush=True)
        PlantedSoleRepair().apply(action)

    @staticmethod
    def retrieve_keys(frames, rotations, tolerance):
        retained = {0, len(frames) - 1}
        pending = [(0, len(frames) - 1)]
        while pending:
            start, end = pending.pop()
            if end > start + 1:
                candidates = []
                for index in range(start + 1, end):
                    weight = (frames[index] - frames[start]) / (frames[end] - frames[start])
                    interpolated = (rotations[start] * (1-weight) + rotations[end] * weight).normalized()
                    error = 2 * math.acos(min(1, abs(interpolated.dot(rotations[index]))))
                    candidates.append((error, index))
                error, index = max(candidates)
                if error > tolerance:
                    retained.add(index)
                    pending.extend(((start, index), (index, end)))
        return sorted(retained)


if __name__ == '__main__':
    main(WaackingArmRepair(), sampling=8)
