"""Resuming installed turn corrections preserves native poses, keys, and timing."""
from pathlib import Path
import sys

import bpy
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'scripts'), str(Path(__file__).parent)]
import repair
import dance_tools
from animation_export_evaluation import AnimationExportEvaluation
from track_chooser import TrackChooser
from new_york_hustle.refine_turn import InsideTurnRefinement
from new_york_hustle.refine_shadow import ShadowRefinement
from salsa.refine_turn import LeaderTurnRefinement


def sample(rigs, frames):
    matrices = []
    for frame in frames:
        bpy.context.scene.frame_set(int(frame), subframe=frame % 1)
        matrices.append(repair.retrieve_matrices(rigs))
    return np.array(matrices)


def main():
    for style, identifier, refinement in (
        ('new_york_hustle', 'new_york_hustle_inside_turn_pass', InsideTurnRefinement()),
        ('new_york_hustle', 'new_york_hustle_shadow_entry_exit', ShadowRefinement()),
        ('salsa', 'salsa_leader_left_turn', LeaderTurnRefinement()),
    ):
        source = ROOT / 'animations' / style / 'sources' / (identifier + '.blend')
        before_hash = repair.digest(source)
        bpy.ops.wm.open_mainfile(filepath=str(source))
        dance_tools.register()
        scene = bpy.context.scene
        TrackChooser(scene).apply(identifier)
        action = bpy.data.actions[identifier]
        repair.bind_source(action)
        rigs = [scene.objects[actor + '.rigify_deform'] for actor in ('Man', 'Woman')]
        controls = [scene.objects[actor + '.rigify'] for actor in ('Man', 'Woman')]
        evaluation = AnimationExportEvaluation(set(rigs + controls))
        evaluation.prepare()
        frames = np.linspace(*action.frame_range, 17)
        timing = (scene.render.fps, scene.render.fps_base, list(action.frame_range))
        counts = [len(curve.keyframe_points) for slot in action.slots for curve in repair.retrieve_curves(action, slot)]
        try:
            original = sample(rigs, frames)
            refinement.apply(action)
            maximum = float(np.abs(sample(rigs, frames) - original).max())
            assert maximum < .00001, (identifier, maximum)
            assert timing == (scene.render.fps, scene.render.fps_base, list(action.frame_range))
            assert counts == [len(curve.keyframe_points) for slot in action.slots for curve in repair.retrieve_curves(action, slot)]
            assert before_hash == repair.digest(source)
            print('RESUME', identifier, 'preserved native poses, key counts, and clock', maximum, flush=True)
        finally:
            evaluation.restore()


if __name__ == '__main__':
    main()
