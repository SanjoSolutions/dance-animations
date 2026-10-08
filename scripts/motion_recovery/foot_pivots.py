"""Author native foot heading while preserving footfall positions and pitch."""
import bpy
from mathutils import Quaternion

from repair import retrieve_curves


class FootPivots:
    def __init__(self, actor):
        self.actor = actor

    def apply(self, action):
        rig = bpy.context.scene.objects[self.actor + '.rigify']
        slot = next(slot for slot in action.slots if slot.identifier == 'OB' + rig.name)
        bones = [rig.pose.bones['foot_ik.' + side] for side in 'LR']
        samples = {bone.name: [] for bone in bones}
        start, end = action.frame_range
        for sample in range(int(start * 2), int(end * 2) + 1):
            frame = sample / 2
            bpy.context.scene.frame_set(int(frame), subframe=frame % 1)
            heading = Quaternion((0, 0, 1), rig.pose.bones['torso'].matrix.to_quaternion().to_euler('XYZ').z)
            for bone in bones:
                rotation = bone.matrix.to_quaternion()
                foot_heading = Quaternion((0, 0, 1), rotation.to_euler('XYZ').z)
                matrix = (heading @ foot_heading.inverted() @ rotation).to_matrix().to_4x4()
                matrix.translation = bone.matrix.translation
                bone.matrix = matrix
                quaternion = bone.rotation_quaternion.copy()
                if samples[bone.name] and quaternion.dot(samples[bone.name][-1][1]) < 0:
                    quaternion.negate()
                samples[bone.name].append((frame, quaternion))
        for bone in bones:
            path = bone.path_from_id('rotation_quaternion')
            for curve in retrieve_curves(action, slot):
                if curve.data_path == path:
                    curve.keyframe_points.clear()
                    curve.keyframe_points.add(len(samples[bone.name]))
                    for point, (frame, quaternion) in zip(curve.keyframe_points, samples[bone.name]):
                        point.co = (frame, quaternion[curve.array_index])
                        point.interpolation = 'LINEAR'
                    curve.update()
