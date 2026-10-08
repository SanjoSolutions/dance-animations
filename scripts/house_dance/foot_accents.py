"""Surface clearance for the woman's articulated toe-support accents."""
import hashlib
import json
from pathlib import Path

from mathutils import Quaternion

from author import HouseAuthor


class FootAccentAuthor(HouseAuthor):
    def targets(self, phrase, actor, frame):
        targets, plants = super().targets(phrase, actor, frame)
        for side in ('left', 'right'):
            foot = targets[side + '_foot']
            relative = Quaternion(foot['rotation']) @ Quaternion(self.base[actor][side + '_foot']['rotation']).inverted()
            pitch = relative.to_euler('XYZ').x
            # The articulated MPFB toes extend below the rigid neutral sole
            # envelope during positive pitch. Fit that measured 10.8 mm peak.
            foot['position'][2] += .011 * min(1, max(0, pitch / .2))
        return targets, plants

    def configure(self, action, phrase, actor):
        recipe = json.loads(action['House recipe'])
        recipe['foot_accents.py'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        action['House recipe'] = json.dumps(recipe, sort_keys=True)
