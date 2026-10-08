"""Keep the raised upper arm's native twist aligned through a leader turn."""
from pathlib import Path
import sys
import math

import bpy
from mathutils import Matrix, Quaternion

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'scripts'), str(ROOT / 'scripts/motion_recovery')]
import repair
from salsa.refine_motion import TurnPivots


class LeaderTurnRefinement:
    def apply(self, action):
        TurnPivots().apply(action)
        if not action.get('Salsa Leader Turn Twist'):
            self.refine_controls(action)

    def refine_controls(self, action):
        scene = bpy.context.scene
        rig = scene.objects['Man.rigify']
        tweak = rig.pose.bones['upper_arm_tweak.L']
        samples = []
        previous_twist = 0.0
        start, end = action.frame_range
        for sample in range(int(start * 4), int(end * 4) + 1):
            frame = sample / 4
            scene.frame_set(int(frame), subframe=frame % 1)
            position, rotation, scale = tweak.matrix.decompose()
            arm = rig.pose.bones['ORG-upper_arm.L'].matrix.to_quaternion()
            difference = rotation.inverted() @ arm
            twist = 2 * math.atan2(difference.y, difference.w)
            twist += round((previous_twist - twist) / math.tau) * math.tau
            previous_twist = twist
            rotation = rotation @ Quaternion((0, 1, 0), twist / 2)
            tweak.matrix = Matrix.LocRotScale(position, rotation, scale)
            previous = samples[-1][1] if samples else tweak.rotation_euler.copy()
            rotation = tweak.rotation_euler.to_quaternion().to_euler(tweak.rotation_mode, previous)
            samples.append((frame, rotation))
        for frame, rotation in samples:
            tweak.rotation_euler = rotation
            tweak.keyframe_insert('rotation_euler', frame=frame, group=tweak.name)
        slot = next(slot for slot in action.slots if slot.identifier == 'OB' + rig.name)
        path = tweak.path_from_id('rotation_euler')
        for curve in repair.retrieve_curves(action, slot):
            if curve.data_path == path:
                for point in curve.keyframe_points:
                    point.interpolation = 'LINEAR'
                curve.update()
        action['Salsa Leader Turn Twist'] = 'Unwrapped IK arm roll shared across the native upper-arm segments'


if __name__ == '__main__':
    repair.main(refinement=LeaderTurnRefinement(), sampling=8)
