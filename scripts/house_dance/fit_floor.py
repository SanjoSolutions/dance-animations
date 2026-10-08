"""Fit floor finger clearance using the evaluated MPFB hand surfaces."""
import json
import math
from pathlib import Path
import sys

import bpy
import numpy as np
from mathutils import Quaternion

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import dance_tools
from track_chooser import TrackChooser


class FingerSurfaceFit:
    def __init__(self, rig):
        self.rig = rig
        self.body = bpy.context.scene.objects[rig.name.split('.')[0] + '.body']
        self.body.hide_viewport = False
        self.body.hide_set(False)
        self.groups = {group.index: group.name for group in self.body.vertex_groups}
        self.indices = {}
        evaluated = self.body.evaluated_get(bpy.context.evaluated_depsgraph_get())
        mesh = evaluated.to_mesh()
        for finger in ('f_index', 'f_middle', 'f_ring', 'f_pinky', 'thumb'):
            for side in 'LR':
                self.indices[finger, side] = [vertex.index for vertex in mesh.vertices
                    if sum(weight.weight for weight in vertex.groups
                           if self.groups[weight.group].startswith('DEF-' + finger)
                           and self.groups[weight.group].endswith('.' + side)) > .5]
        evaluated.to_mesh_clear()

    def retrieve_height(self, finger, side):
        self.rig.update_tag()
        bpy.context.view_layer.update()
        evaluated = self.body.evaluated_get(bpy.context.evaluated_depsgraph_get())
        mesh = evaluated.to_mesh()
        coordinates = np.empty(len(mesh.vertices) * 3)
        mesh.vertices.foreach_get('co', coordinates)
        points = coordinates.reshape((-1, 3))[self.indices[finger, side]]
        transform = np.array(evaluated.matrix_world)
        heights = points @ transform[2, :3] + transform[2, 3]
        evaluated.to_mesh_clear()
        return float(heights.min())

    def fit(self):
        result = {}
        for finger in ('f_index', 'f_middle', 'f_ring', 'f_pinky', 'thumb'):
            for side in 'LR':
                bone = self.rig.pose.bones[finger + '.01.' + side]
                initial = bone.rotation_quaternion.copy()
                angles = [0.0, 0.0, 0.0]
                height = self.retrieve_height(finger, side)
                initial_height = height
                cost = abs(height - .002) + 4 * max(0, -height)
                for step in (10, 5, 2, 1):
                    for axis in range(3):
                        for sign in (-1, 1):
                            candidate = angles.copy()
                            candidate[axis] += sign * math.radians(step)
                            rotation = initial.copy()
                            for index, angle in enumerate(candidate):
                                vector = [0, 0, 0]
                                vector[index] = 1
                                rotation = rotation @ Quaternion(vector, angle)
                            bone.rotation_quaternion = rotation
                            candidate_height = self.retrieve_height(finger, side)
                            candidate_cost = abs(candidate_height - .002) + 4 * max(0, -candidate_height)
                            if candidate_cost < cost:
                                angles, cost, height = candidate, candidate_cost, candidate_height
                rotation = initial.copy()
                for axis, angle in enumerate(angles):
                    vector = [0, 0, 0]
                    vector[axis] = 1
                    rotation = rotation @ Quaternion(vector, angle)
                bone.rotation_quaternion = rotation
                bone.keyframe_insert('rotation_quaternion', frame=0, group=bone.name)
                result[bone.name] = dict(rotation=list(rotation), before=initial_height,
                                         after=self.retrieve_height(finger, side))
                print('FINGER', bone.name, result[bone.name], flush=True)
        return result


def main():
    actor = sys.argv[sys.argv.index('--') + 1]
    name = f'house_{actor}_floor_support_position'
    source = ROOT / '.cache/house/candidates/sources' / (name + '.blend')
    bpy.ops.wm.open_mainfile(filepath=str(source))
    dance_tools.register()
    TrackChooser(bpy.context.scene).apply(name)
    rig = bpy.context.scene.objects[actor.capitalize() + '.rigify']
    for obj in bpy.context.scene.objects:
        if obj.type == 'ARMATURE':
            obj.hide_viewport = False
            obj.hide_set(False)
    action = bpy.data.actions[name]
    rig.animation_data.action = action
    rig.animation_data.action_slot = next(slot for slot in action.slots if slot.identifier == 'OB' + rig.name)
    rig.animation_data.use_nla = False
    bpy.context.scene.frame_set(0)
    result = FingerSurfaceFit(rig).fit()
    destination = Path(__file__).with_name('floor_fingers_' + actor + '.json')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    dance_tools.save_source(action, ROOT / '.cache/house/fitted/sources' / source.name)


if __name__ == '__main__':
    main()
