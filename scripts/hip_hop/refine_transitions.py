"""Align wide-stance transitions with their actual saved entry and exit poses."""
import json
from pathlib import Path
import sys

import bpy

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/motion_recovery'))
import repair


class TransitionEndpoints:
    def apply(self, action):
        identifier = action.name
        actor, move = identifier.removeprefix('hip_hop_').split('_', 1)
        names = [f'hip_hop_{actor}_pose_{pose}' for pose in move.split('_to_')]
        references = []
        for name in names:
            source = ROOT / 'animations/hip_hop/sources' / (name + '.blend')
            with bpy.data.libraries.load(str(source), link=False) as (available, loaded):
                loaded.actions = [name]
            reference = loaded.actions[0]
            repair.ConstantRotationRepair(reference).apply()
            references.append(reference)
        start, end = action.frame_range
        for slot in action.slots:
            targets = [{(curve.data_path, curve.array_index): curve.evaluate(reference.frame_start)
                        for curve in repair.retrieve_curves(reference, next(candidate for candidate in reference.slots if candidate.identifier == slot.identifier))}
                       for reference in references]
            for curve in repair.retrieve_curves(action, slot):
                key = (curve.data_path, curve.array_index)
                if all(key in target for target in targets):
                    first, last = [target[key] for target in targets]
                    changes = (first - curve.evaluate(start), last - curve.evaluate(end))
                    if len(curve.keyframe_points) == 1 and abs(first - last) > 1e-7:
                        curve.keyframe_points.insert(end, curve.evaluate(end))
                    for point in curve.keyframe_points:
                        amount = (point.co.x - start) / (end - start)
                        correction = changes[0] * (1 - amount) + changes[1] * amount
                        point.co.y += correction
                        point.handle_left.y += correction
                        point.handle_right.y += correction
                    curve.update()
        for reference in references:
            bpy.data.actions.remove(reference)
        repair.bind_source(action)
        action['Transition Endpoints'] = json.dumps(names)


if __name__ == '__main__':
    repair.main(refinement=TransitionEndpoints(), sampling=2)
