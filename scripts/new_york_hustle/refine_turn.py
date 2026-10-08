"""Keep the follower's feet aligned through the inside-turn pass."""
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'scripts'), str(ROOT / 'scripts/motion_recovery')]
import repair
from new_york_hustle.refine_motion import HustleMotionRefinement
from foot_pivots import FootPivots


class InsideTurnRefinement:
    def apply(self, action):
        HustleMotionRefinement().apply(action)
        if not action.get('Hustle Inside Turn Pivots'):
            FootPivots('Woman').apply(action)
            action['Hustle Inside Turn Pivots'] = 'Follower foot heading follows torso; footfalls and hand targets retained'


if __name__ == '__main__':
    repair.main(refinement=InsideTurnRefinement(), sampling=8)
