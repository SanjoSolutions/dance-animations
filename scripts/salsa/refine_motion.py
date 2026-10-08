"""Keep turning feet aligned with the dancer through native IK pivots."""

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/motion_recovery'))
import repair
from sole_calibration import SoleCalibration
from foot_pivots import FootPivots


class TurnPivots:
    """Preserve footfall positions and pitch while the planted sole pivots."""

    def apply(self, action):
        figure = json.loads(action['Salsa'])
        if figure['figure'] == 'turn' and not action.get('Salsa Turn Pivots'):
            actor = 'Man' if figure['turning_actor'] == 'player' else 'Woman'
            FootPivots(actor).apply(action)
            action['Salsa Turn Pivots'] = 'Footfall positions and pitch retained; heading follows torso through planted pivots'

        SoleCalibration(.020).apply(action)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('identifier')
    parser.add_argument('--sampling', type=int, default=4)
    arguments = parser.parse_args(sys.argv[sys.argv.index('--') + 1:])
    repair.main(refinement=TurnPivots(), sampling=arguments.sampling)
