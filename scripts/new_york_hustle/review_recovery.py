"""Check preserved hand contacts and near-seam velocities at the source's rate."""

import json
import math
from pathlib import Path
import sys

import bpy
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'scripts/motion_recovery'), str(Path(__file__).parent)]
from repair import retrieve_matrices
import dance_tools
from polish import GripTiming
from snap_hand import HandSnap
from animation_export_evaluation import AnimationExportEvaluation
from track_chooser import TrackChooser


def main():
    identifier = sys.argv[sys.argv.index('--') + 1]
    directory = ROOT / '.cache/motion-recovery' / identifier
    report = json.loads((directory / 'checkpoint.json').read_text())
    bpy.ops.wm.open_mainfile(filepath=str(ROOT / report['source']))
    dance_tools.register()
    scene = bpy.context.scene
    TrackChooser(scene).apply(identifier)
    controls = [scene.objects[actor + '.rigify'] for actor in ('Man', 'Woman')]
    rigs = [scene.objects[actor + '.rigify_deform'] for actor in ('Man', 'Woman')]
    hands = {(actor, side): HandSnap(bpy.context, rig, side) for actor, rig in zip(('Man','Woman'), controls) for side in 'LR'}
    timing = GripTiming(identifier)
    rate = scene.render.fps / scene.render.fps_base
    evaluation = AnimationExportEvaluation(set(controls + rigs))
    evaluation.prepare()
    maximum_gap = 0
    contact_samples = 0
    worst_frame = 0
    try:
        for frame in report['sampledFrames']:
            scene.frame_set(int(frame), subframe=frame % 1)
            for leader, follower, weight, _heading in timing.retrieve_contacts(frame * 24 / rate):
                if weight == 1:
                    first, second = hands['Man', leader], hands['Woman', follower]
                    gap = ((first.retrieve_hand_pose() @ first.wrist.inverted()).translation - (second.retrieve_hand_pose() @ second.wrist.inverted()).translation).length
                    contact_samples += 1
                    if gap > maximum_gap:
                        maximum_gap, worst_frame = gap, frame
        seam_velocity = None
        if report['loop']:
            start, end = report['storedRange']
            step = .01 * rate / 24
            matrices = []
            for frame in (start, start + step, end - step, end):
                scene.frame_set(int(frame), subframe=frame % 1)
                matrices.append(retrieve_matrices(rigs)[..., :3, 3])
            seam_velocity = float(np.linalg.norm(((matrices[1] - matrices[0]) - (matrices[3] - matrices[2])) / (step / rate), axis=-1).max())
    finally:
        evaluation.restore()
    result = dict(sourceSha256=report['sourceSha256'], contactSamples=contact_samples, maximumPalmGap=maximum_gap,
                  worstFrame=worst_frame, loopVelocityDifference=seam_velocity, units='meters and meters/second',
                  limits=dict(maximumPalmGap=.025, loopVelocityDifference=.12),
                  passed=maximum_gap < .025 and (seam_velocity is None or seam_velocity < .12))
    (directory / 'contacts.json').write_text(json.dumps(result, indent=2) + '\n')
    print('CONTACTS', identifier, json.dumps(result), flush=True)
    assert result['passed'], result


if __name__ == '__main__':
    main()
