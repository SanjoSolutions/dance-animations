"""Supported lofting phrases using calibrated palm contacts and open fingers."""
import math
import json
import sys
from pathlib import Path
import bpy
from mathutils import Quaternion
from snap_hand import HandSnap
from contacts import FloorSurface
sys.path.insert(0,str(Path(__file__).resolve().parent))
from author import HouseAuthor, END
from repertoire import Phrase
from animation_wrist_constraints import AnimationWristConstraints

from repertoire import FLOOR_PHRASES


class FloorAuthor(HouseAuthor):
    def configure(self,action,phrase,actor):
        # Standing wrist constraints exclude the extension needed for palm support.
        # Calibrated palm frames and evaluated wrist/hand geometry govern this pose.
        self.author.solver.angular_tolerance = .003
        action['animation_wrist_constraint']=False
        AnimationWristConstraints(bpy.context.scene).apply(action)
        rig=self.author.rigs[actor]
        for bone in rig.pose.bones:
            if bone.name.startswith(('f_index.','f_middle.','f_ring.','f_pinky.','thumb.')):
                bone.rotation_quaternion=Quaternion()
                bone.rotation_euler=(0,0,0)
                path='rotation_quaternion' if bone.rotation_mode=='QUATERNION' else 'rotation_euler'
                bone.keyframe_insert(path,frame=0)
        targets, _ = self.targets(phrase, actor, 0)
        keyed, _ = self.author.solve(actor, targets)
        for bone, path in keyed:
            bone.keyframe_insert(path, frame=0, group=bone.name)
        for side in 'LR':
            hand = HandSnap(bpy.context, rig, side)
            palm = hand.retrieve_hand_pose() @ hand.wrist.inverted()
            hand.fit_fingers(FloorSurface(), palm)
            for name in hand.calibration['fingers']:
                bone = rig.pose.bones[name]
                rotation = 'rotation_quaternion' if bone.rotation_mode == 'QUATERNION' else 'rotation_euler'
                for path in ('location', rotation):
                    bone.keyframe_insert(path, frame=0, group=name)
        character = 'man' if actor == 'player' else 'woman'
        corrections = json.loads(Path(__file__).with_name('floor_fingers_' + character + '.json').read_text())
        for name, correction in corrections.items():
            bone = rig.pose.bones[name]
            bone.rotation_quaternion = Quaternion(correction['rotation'])
            bone.keyframe_insert('rotation_quaternion', frame=0, group=name)

    def targets(self,phrase,actor,frame):
        phase=math.tau*frame/END
        pulse=math.sin(phase)**2
        rock=.015*math.sin(phase)**3 if phrase.name=='lofting_floor_rock' else 0
        wave=.015*pulse if phrase.name=='lofting_body_wave' else 0
        tilt=math.radians(70)+(.08*math.sin(phase)**3 if wave else 0)
        targets={
            'torso':{'position':[0,.1+rock,.36+wave],'rotation':list(Quaternion((1,0,0),tilt))},
            'chest':{'rotation':list(Quaternion((1,0,0),tilt))},
            'hips':{'rotation':list(Quaternion((1,0,0),tilt))},
            'head':{'rotation':list(Quaternion((1,0,0),math.radians(155)))},
        }
        plants={}
        for side,sign in (('left',1),('right',-1)):
            sweep=pulse if phrase.name=='lofting_leg_sweep_'+side else 0
            switch=max(0,sign*math.sin(phase))**2 if phrase.name=='lofting_knee_switch' else 0
            targets[side+'_foot']={'position':[sign*(.24+.17*sweep),.47-.13*sweep-.12*switch,self.soles.retrieve_height(actor, side, Quaternion(self.base[actor][side+'_foot']['rotation']))+.045*max(sweep,switch)],'rotation':self.base[actor][side+'_foot']['rotation']}
            targets[side+'_knee']={'position':[sign*.35,-.7,.65 if actor == 'player' else .2]}
            targets[side+'_palm']={'position':[sign*.29,-.40,.0585 if actor == 'player' else .050],'rotation':list(Quaternion((1,0,0),math.pi))}
            targets[side+'_elbow']={'position':[sign*.55,-.15,.42]}
            plants[side]=max(sweep,switch)<1e-7
        return targets,plants

    def run(self,names):
        try:
            for phrase in FLOOR_PHRASES:
                if not names or phrase.name in names:
                    for actor in ('player','partner'):
                        self.create(phrase,actor)
        finally:
            self.evaluation.restore()


if __name__=='__main__':
    FloorAuthor().run(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
