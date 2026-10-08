"""Close native Hustle loop endpoints and preserve fast hand arcs in denser bakes."""

from pathlib import Path
import sys

import bpy

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/motion_recovery'))
import repair
from sole_calibration import SoleCalibration


class LoopClosure:
    """Preserve complete turns while matching the repeated closing control pose."""

    def apply(self, action):
        start, end = action.frame_range
        changed = 0
        if action.use_cyclic and not action.get('Hustle Loop Hold'):
            if not action.get('Hustle Seam Ease'):
                self.ease_key_times(action, start, end)
                action['Hustle Seam Ease'] = 4
            for slot in action.slots:
                curves = repair.retrieve_curves(action, slot)
                quaternion_signs = {}
                for path in {curve.data_path for curve in curves if curve.data_path.endswith('rotation_quaternion')}:
                    rotations = sorted((curve for curve in curves if curve.data_path == path), key=lambda curve: curve.array_index)
                    first = [curve.evaluate(start) for curve in rotations]
                    previous = [curve.evaluate(end - .1) for curve in rotations]
                    quaternion_signs[path] = -1 if sum(a*b for a,b in zip(first, previous)) < 0 else 1
                for curve in curves:
                    points = curve.keyframe_points
                    if len(points) > 1 and abs(points[-1].co.x - end) < .0001:
                        target = curve.evaluate(start) * quaternion_signs.get(curve.data_path, 1)
                        point = points[-1]
                        difference = target - point.co.y
                        if abs(difference) > 1e-8:
                            point.co.y = target
                            point.handle_left.y += difference
                            point.handle_right.y += difference
                            changed += 1
                        if abs(points[0].co.x - start) < .0001:
                            first = points[0]
                            first.interpolation = 'BEZIER'
                            points[-2].interpolation = 'BEZIER'
                            incoming = (end - points[-2].co.x) / 3
                            outgoing = (points[1].co.x - start) / 3
                            first.handle_left_type = first.handle_right_type = 'FREE'
                            point.handle_left_type = point.handle_right_type = 'FREE'
                            first.handle_left = (start - incoming, first.co.y)
                            first.handle_right = (start + outgoing, first.co.y)
                            point.handle_left = (end - incoming, point.co.y)
                            point.handle_right = (end + outgoing, point.co.y)
                        curve.update()
                        for frame, value in ((start + .5, curve.evaluate(start)), (end - .5, curve.evaluate(end))):
                            hold = curve.keyframe_points.insert(frame, value)
                            hold.interpolation = 'BEZIER'
                            hold.handle_left_type = hold.handle_right_type = 'AUTO_CLAMPED'
                        curve.keyframe_points[-3].interpolation = 'BEZIER'
                        curve.update()
            action['Hustle Loop Hold'] = .5
        action['Hustle Loop Closure'] = changed
        action['Motion Recovery'] = 'Closed native loop endpoints; dense hand-arc sampling; procedural study'
        return changed


    @staticmethod
    def ease_key_times(action, start, end):
        span = min(4, (end - start) / 4)
        def expand(value):
            low, high = 0.0, 1.0
            for _ in range(24):
                middle = (low + high) / 2
                if middle * middle * (2 - middle) < value:
                    low = middle
                else:
                    high = middle
            return (low + high) / 2
        def remap(frame):
            if start < frame < start + span:
                return start + .5 + (span - .5) * expand((frame - start) / span)
            if end - span < frame < end:
                return end - .5 - (span - .5) * expand((end - frame) / span)
            return frame
        for slot in action.slots:
            for curve in repair.retrieve_curves(action, slot):
                for point in curve.keyframe_points:
                    coordinate, left, right = point.co.x, point.handle_left.x, point.handle_right.x
                    point.co.x = remap(coordinate)
                    point.handle_left.x = remap(left)
                    point.handle_right.x = remap(right)
                curve.update()


class HustleMotionRefinement:
    def __init__(self):
        self.loops = LoopClosure()
        self.soles = SoleCalibration(.016)

    def apply(self, action):
        self.loops.apply(action)
        self.soles.apply(action)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('identifier')
    parser.add_argument('--sampling', type=int, default=4)
    arguments = parser.parse_args(sys.argv[sys.argv.index('--') + 1:])
    repair.main(refinement=HustleMotionRefinement(), sampling=arguments.sampling)
