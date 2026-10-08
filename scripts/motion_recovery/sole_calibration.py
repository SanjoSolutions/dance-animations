"""Adjust native foot IK height against the measured MPFB soles."""
import json

import bpy
from mathutils import Vector

from repair import retrieve_curves


class SoleCalibration:
    def __init__(self, lift):
        self.lift = lift

    def apply(self, action):
        rig = bpy.context.scene.objects['Man.rigify']
        slot = next(slot for slot in action.slots if slot.identifier == 'OB' + rig.name)
        bpy.context.scene.frame_set(int(action.frame_start))
        previous = json.loads(action.get('MPFB Sole Calibration', '{}')).get('worldLift', 0)
        changes = {}
        for side in 'LR':
            bone = rig.pose.bones['foot_ik.' + side]
            location = bone.location.copy()
            target = bone.matrix.copy()
            target.translation += Vector((0, 0, self.lift - previous))
            bone.matrix = target
            offset = bone.location - location
            bone.location = location
            path = bone.path_from_id('location')
            for curve in retrieve_curves(action, slot):
                if curve.data_path == path:
                    difference = offset[curve.array_index]
                    for point in curve.keyframe_points:
                        point.co.y += difference
                        point.handle_left.y += difference
                        point.handle_right.y += difference
                    curve.update()
            changes[bone.name] = list(offset)
        action['MPFB Sole Calibration'] = json.dumps(dict(worldLift=self.lift, localOffsets=changes))
