"""Planted entry, level-change, and recovery clips for the House phrase graph."""
import sys
from pathlib import Path
from dataclasses import replace
sys.path.insert(0,str(Path(__file__).resolve().parent))
from author import HouseAuthor, END, smooth
from repertoire import Phrase

from repertoire import TRANSITIONS


class TransitionAuthor(HouseAuthor):
    def configure(self,action,phrase,actor):
        action['House loop']=False

    def targets(self,phrase,actor,frame):
        first,last=TRANSITIONS[phrase.name]
        depth=first+(last-first)*smooth(frame/END)
        return super().targets(replace(phrase,family='positions',depth=depth),actor,frame)

    @staticmethod
    def finish_curves(action):
        HouseAuthor.finish_curves(action, loop=False)

    def review(self,phrase,actor,action):
        report=super().review(phrase,actor,action)
        report['loop']=False
        report['passed']=(report['plant_error']<.003 and report['minimum_ankle_separation']>.15
            and report['maximum_half_frame_displacement']<.12
            and report['minimum_hand_torso_proxy_clearance']>.025
            and report['joint_angle_range'][0]>.25 and report['joint_angle_range'][1]<3.13)
        return report

    def run(self,names):
        try:
            for name in TRANSITIONS:
                if not names or name in names:
                    for actor in ('player','partner'):
                        self.create(Phrase(name,'transitions'),actor)
        finally:
            self.evaluation.restore()


if __name__=='__main__':
    TransitionAuthor().run(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
