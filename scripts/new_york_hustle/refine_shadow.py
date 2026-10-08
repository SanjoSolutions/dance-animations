"""Keep the follower's returning shadow hold on a stable native elbow arc."""
from pathlib import Path
import sys

import bpy

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'scripts'), str(ROOT / 'scripts/motion_recovery')]
import repair
from new_york_hustle.refine_motion import HustleMotionRefinement
from new_york_hustle.polish import BoneKeys, HandPose


class ShadowRefinement:
    def apply(self, action):
        HustleMotionRefinement().apply(action)
        if not action.get('Hustle Shadow Elbow'):
            self.refine_controls(action)

    def refine_controls(self, action):
        scene = bpy.context.scene
        rig = scene.objects['Woman.rigify']
        samples = []
        start, end = action.frame_range
        for sample in range(int(start * 2), int(end * 2) + 1):
            frame = sample / 2
            scene.frame_set(int(frame), subframe=frame % 1)
            hand = HandPose(rig, 'L', BoneKeys(frame, {}))
            samples.append((frame, hand.retrieve_palm().translation.copy()))
        rotations = {}
        for frame, position in samples:
            scene.frame_set(int(frame), subframe=frame % 1)
            keys = BoneKeys(frame, rotations)
            hand = HandPose(rig, 'L', keys)
            hand.place_elbow(0)
            hand.place_position(position)
            rotations.update(keys.current_rotations)
        slot = next(slot for slot in action.slots if slot.identifier == 'OB' + rig.name)
        paths = {rig.pose.bones[name].path_from_id('location') for name in ('hand_ik.L', 'upper_arm_ik_target.L')}
        for curve in repair.retrieve_curves(action, slot):
            if curve.data_path in paths:
                for point in curve.keyframe_points:
                    point.interpolation = 'LINEAR'
                curve.update()
        action['Hustle Shadow Elbow'] = 'Follower left palm and wrist retained; elbow follows a stable torso-relative arc'


if __name__ == '__main__':
    repair.main(refinement=ShadowRefinement(), sampling=8)
