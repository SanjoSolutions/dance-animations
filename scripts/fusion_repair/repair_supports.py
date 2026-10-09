"""Fit Fusion support curves in world space and use the native bake pipeline."""
import json
import math
from pathlib import Path
import sys

import bpy
import numpy as np
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/motion_recovery'))
import repair

STEPPING = {'fusion_box_basic', 'fusion_forward_back_basic', 'fusion_promenade_walk',
            'fusion_shadow_walk', 'fusion_side_basic', 'fusion_triple_step'}


def write_curve(curve, times, values, slopes):
    curve.keyframe_points.clear()
    if max(values) - min(values) < 1e-8 and max(abs(value) for value in slopes) < 1e-8:
        point = curve.keyframe_points.insert(times[0], values[0])
        point.interpolation = 'CONSTANT'
    else:
        curve.keyframe_points.add(len(times))
        for index, (point, time, value, slope) in enumerate(zip(curve.keyframe_points, times, values, slopes)):
            before = (time - times[index - 1]) / 3 if index else (times[1] - time) / 3
            after = (times[index + 1] - time) / 3 if index + 1 < len(times) else before
            point.co = (time, value)
            point.interpolation = 'BEZIER'
            point.handle_left_type = point.handle_right_type = 'FREE'
            point.handle_left = (time - before, value - before * slope)
            point.handle_right = (time + after, value + after * slope)
    curve.update()


class FusionRotationRepair:
    """Preserve active quaternion fingers and remove their inactive held Euler keys."""

    def __init__(self, action):
        self.action = action

    def apply(self):
        removed = []
        for slot in self.action.slots:
            owner = bpy.context.scene.objects[slot.identifier[2:]]
            curves = repair.retrieve_curves(self.action, slot)
            for curve in curves:
                if curve.data_path.endswith('.rotation_euler') and len(curve.keyframe_points) == 1:
                    bone = owner.pose.bones[curve.data_path.split('"')[1]]
                    quaternion_path = bone.path_from_id('rotation_quaternion')
                    if bone.rotation_mode == 'QUATERNION' and any(item.data_path == quaternion_path for item in curves):
                        for layer in self.action.layers:
                            for strip in layer.strips:
                                for bag in strip.channelbags:
                                    if bag.slot_handle == slot.handle:
                                        removed.append(dict(owner=owner.name, bone=bone.name, component=curve.array_index, value=curve.keyframe_points[0].co.y))
                                        bag.fcurves.remove(curve)
        self.action['Fusion active rotation channels'] = json.dumps(removed)
        return repair.ConstantRotationRepair(self.action).apply()


class FootPhrase:
    """Stationary supports alternating with eased swing and landing poses."""

    def __init__(self, initial, landings, side):
        self.initial = np.array(initial)
        self.landings = landings
        self.side = side

    def retrieve(self, time):
        position = self.initial.copy()
        velocity = np.zeros(3)
        start = 0
        for index, (end, target) in enumerate(self.landings):
            if index % 2 == self.side:
                if time >= end:
                    position = np.array(target)
                elif time > start:
                    phase = (time - start) / (end - start)
                    difference = np.array(target) - position
                    velocity = difference * (6 * phase * (1 - phase) / (end - start))
                    position += difference * (phase * phase * (3 - 2 * phase))
                    position[2] += .045 * math.sin(math.pi * phase) ** 2
                    velocity[2] += .045 * math.pi * math.sin(2 * math.pi * phase) / (end - start)
            start = end
        return position, velocity

    def retrieve_supports(self):
        intervals = []
        start = 0
        for index, (end, _) in enumerate(self.landings):
            if index % 2 != self.side:
                intervals.append([start, end])
            start = end
        return intervals or [[0, 96]]


class NativeLegScaleFit:
    """Keep native IK leg lengths aligned with the connected deformation skeleton."""

    @staticmethod
    def fit_current(rig):
        deform = bpy.context.scene.objects[rig.name + '_deform']
        for side in 'LR':
            bone = rig.pose.bones['thigh_ik.' + side]
            for iteration in range(10):
                factor = 1 / bone.matrix.to_scale().y
                if abs(factor - 1) > .000002:
                    bone.scale *= factor
                    rig.update_tag()
                    deform.update_tag()
                    bpy.context.view_layer.update()

    def apply(self, action):
        from animation_export_evaluation import AnimationExportEvaluation
        scene = bpy.context.scene
        rigs = {scene.objects[actor + suffix] for actor in ('Man', 'Woman') for suffix in ('.rigify', '.rigify_deform')}
        evaluation = AnimationExportEvaluation(rigs)
        evaluation.prepare()
        times = np.arange(0, 96.01, 1.5 if action.name == 'fusion_triple_step' else 3)
        result = {}
        try:
            for slot in action.slots:
                rig = scene.objects[slot.identifier[2:]]
                values = {side: [] for side in 'LR'}
                maximum = 0
                for time in times:
                    scene.frame_set(int(time), subframe=time % 1)
                    self.fit_current(rig)
                    for side in 'LR':
                        bone = rig.pose.bones['thigh_ik.' + side]
                        values[side].append(list(bone.scale))
                        maximum = max(maximum, abs(bone.matrix.to_scale().y - 1))
                for side in 'LR':
                    scales = np.array(values[side])
                    scales[-1] = scales[0]
                    slopes = np.gradient(scales, times, axis=0)
                    slopes[0] = slopes[-1] = 0
                    for curve in repair.retrieve_curves(action, slot):
                        if curve.data_path == rig.pose.bones['thigh_ik.' + side].path_from_id('scale'):
                            write_curve(curve, times, scales[:, curve.array_index], slopes[:, curve.array_index])
                if maximum > .0002:
                    raise ValueError('Native leg reach requires closer landing targets: ' + rig.name + ' ' + str(maximum))
                result[rig.name] = dict(maximumLongitudinalScaleError=maximum, correctiveKeys=len(times), minimumControlScale=float(np.min(list(values.values()))), maximumControlScale=float(np.max(list(values.values()))))
        finally:
            evaluation.restore()
        return result


class FusionSupportRepair:
    def apply(self, action):
        scene = bpy.context.scene
        stepping = action.name in STEPPING
        triple = action.name == 'fusion_triple_step'
        times = np.arange(0, 96.01, 3 if triple else 6)
        boundaries = [12, 24, 30, 36, 48, 60, 72, 78, 84, 96] if triple else list(range(12, 97, 12))
        plan = dict(tempo=120, beats=8, originalRate=24, duration=4, formation=action.get('fusion_start_position'),
                    phrase='1, 2, 3-and-4, 5, 6, 7-and-8' if triple else 'recorded eight-beat Fusion phrase',
                    boundaries=boundaries if stepping else [], supports={}, soleCalibration={}, units='meters')
        for slot in action.slots:
            rig = scene.objects[slot.identifier[2:]]
            curves = repair.retrieve_curves(action, slot)
            roots = sorted([curve for curve in curves if curve.data_path == 'pose.bones["root"].location'], key=lambda curve: curve.array_index)
            root_values = np.array([[curve.evaluate(time) for curve in roots] for time in times])
            root_slopes = np.array([[(curve.evaluate(time + .001) - curve.evaluate(time - .001)) / .002 for curve in roots] for time in times])
            root_values[-1] = root_values[0]
            root_slopes[0] = root_slopes[-1] = 0
            scene.frame_set(0)
            root = rig.pose.bones['root']
            root_basis = (rig.matrix_world @ root.bone.matrix_local).to_3x3()
            initial_positions = {}
            foot_settings = {}
            for side in 'LR':
                foot = rig.pose.bones['foot_ik.' + side]
                initial_positions[side] = np.array((rig.matrix_world @ foot.matrix).translation)
                initial_location = np.array(foot.location)
                columns = []
                for axis in range(3):
                    foot.location[axis] += .01
                    bpy.context.view_layer.update()
                    columns.append((np.array((rig.matrix_world @ foot.matrix).translation) - initial_positions[side]) / .01)
                    foot.location[axis] -= .01
                    bpy.context.view_layer.update()
                foot_settings[side] = (initial_location, np.linalg.inv(np.array(columns).T), list(foot.rotation_quaternion))
            NativeLegScaleFit.fit_current(rig)
            for side in 'LR':
                bone = rig.pose.bones['thigh_ik.' + side]
                for curve in curves:
                    if curve.data_path == bone.path_from_id('scale'):
                        write_curve(curve, [0], [bone.scale[curve.array_index]], [0])
            body = scene.objects[rig.name.split('.')[0] + '.body']
            calibration_body = body.copy()
            calibration_body.name = 'Fusion sole calibration'
            scene.collection.objects.link(calibration_body)
            calibration_body.hide_set(False)
            calibration_body.hide_viewport = False
            for modifier in calibration_body.modifiers:
                if modifier.name.startswith('Delete.'):
                    modifier.show_viewport = False
            bpy.context.view_layer.update()
            graph = bpy.context.evaluated_depsgraph_get()
            evaluated = calibration_body.evaluated_get(graph)
            mesh = evaluated.to_mesh()
            vertices = np.array([list(evaluated.matrix_world @ vertex.co) for vertex in mesh.vertices])
            evaluated.to_mesh_clear()
            bpy.data.objects.remove(calibration_body, do_unlink=True)
            lifts = {}
            for side, position in initial_positions.items():
                mask = (np.linalg.norm(vertices[:, :2] - position[:2], axis=1) < .23) & (vertices[:, 2] < .2)
                if not mask.any():
                    raise ValueError('Calibrated sole coverage required: ' + rig.name + side)
                lifts[side] = .002 - float(vertices[mask, 2].min())
            plan['soleCalibration'][rig.name] = lifts
            targets = {side: [] for side in 'LR'}
            for index, frame in enumerate(boundaries):
                scene.frame_set(frame)
                for side in 'LR':
                    position = np.array((rig.matrix_world @ rig.pose.bones['foot_ik.' + side].matrix).translation)
                    position[2] = initial_positions[side][2] + lifts[side]
                    if triple:
                        support_end = boundaries[index + 1] if index + 1 < len(boundaries) else 96
                        midpoint = (frame + support_end) / 2
                        displacement = Vector([curve.evaluate(midpoint) - curve.evaluate(0) for curve in roots])
                        position = initial_positions[side] + np.array(root_basis @ displacement) + np.array([0, 0, lifts[side]])
                    if frame >= (84 if not triple else 84):
                        position = initial_positions[side] + np.array([0, 0, lifts[side]])
                    targets[side].append((frame, position.tolist()))
            for axis, curve in enumerate(roots):
                write_curve(curve, times, root_values[:, axis], root_slopes[:, axis])
            for side_index, side in enumerate('LR'):
                initial_location, inverse, quaternion = foot_settings[side]
                initial = initial_positions[side] + np.array([0, 0, lifts[side]])
                phrase = FootPhrase(initial, targets[side] if stepping else [], side_index)
                values, slopes = [], []
                for index, time in enumerate(times):
                    position, velocity = phrase.retrieve(time)
                    root_offset = np.array(root_basis @ Vector(root_values[index] - root_values[0]))
                    root_velocity = np.array(root_basis @ Vector(root_slopes[index]))
                    values.append(initial_location + inverse @ (position - initial_positions[side] - root_offset))
                    slopes.append(inverse @ (velocity - root_velocity))
                values, slopes = np.array(values), np.array(slopes)
                foot = rig.pose.bones['foot_ik.' + side]
                for curve in curves:
                    if curve.data_path == foot.path_from_id('location'):
                        write_curve(curve, times, values[:, curve.array_index], slopes[:, curve.array_index])
                    elif curve.data_path == foot.path_from_id('rotation_quaternion'):
                        write_curve(curve, [0], [quaternion[curve.array_index]], [0])
                plan['supports'][rig.name + '/' + side] = phrase.retrieve_supports()
            # Synchronize the repeated endpoint and ease its two approach tangents.
            for curve in curves:
                points = curve.keyframe_points
                if len(points) > 1 and abs(points[-1].co.x - 96) < .001:
                    last, first = points[-1], points[0]
                    difference = first.co.y - last.co.y
                    last.co.y += difference
                    last.handle_left.y += difference
                    last.handle_right.y += difference
                    for point in (first, last):
                        point.handle_left_type = point.handle_right_type = 'FREE'
                        point.handle_left.y = point.handle_right.y = point.co.y
                    curve.update()
        plan['nativeLegScaleFit'] = NativeLegScaleFit().apply(action)
        action['Fusion support plan'] = json.dumps(plan)
        action['animation_loop_end_exclusive'] = True


if __name__ == '__main__':
    identifier = sys.argv[sys.argv.index('--') + 1]
    repair.main(refinement=FusionSupportRepair(), sampling=8 if identifier == 'fusion_triple_step' else 2, rotation_repair=FusionRotationRepair)
