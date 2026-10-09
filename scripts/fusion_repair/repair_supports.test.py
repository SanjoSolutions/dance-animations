"""Verify held support and the half-beat landing through the phrase API."""
from pathlib import Path
import sys
import unittest
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from repair_supports import FootPhrase


class FootPhraseTests(unittest.TestCase):
    def test_support_retains_its_landing_position_and_velocity(self):
        phrase=FootPhrase([0,0,0],[(12,[.12,0,0]),(24,[.24,0,0])],0)
        for frame in (12,12.5,18,23.5,24):
            position,velocity=phrase.retrieve(frame)
            np.testing.assert_allclose(position,[.12,0,0],atol=1e-12)
            np.testing.assert_allclose(velocity,[0,0,0],atol=1e-12)

    def test_syncopated_foot_lands_on_the_half_beat(self):
        phrase=FootPhrase([0,0,0],[(12,[.04,0,0]),(24,[.14,0,0]),(30,[.08,0,0]),(36,[.18,0,0])],0)
        self.assertGreater(phrase.retrieve(27)[0][2],.04)
        np.testing.assert_allclose(phrase.retrieve(30)[0],[.08,0,0],atol=1e-12)
        np.testing.assert_allclose(phrase.retrieve(30)[1],[0,0,0],atol=1e-12)
        self.assertIn([30,36],phrase.retrieve_supports())


if __name__=='__main__':
    unittest.main(argv=[sys.argv[0]])
