"""Author solo House phrases with the shared Blender 5.2 IK/file helpers.

blender -b --factory-startup --python scripts/house_dance/build_clip.py -- CLIP_ID
"""
import json
import hashlib
import math
from pathlib import Path
import sys
from copy import deepcopy
import bpy
from mathutils import Quaternion, Vector

DIRECTORY = Path(__file__).resolve().parent
PROJECT = DIRECTORY.parents[1]
sys.path.insert(0, str(DIRECTORY))
sys.path.insert(0, str(DIRECTORY.parent))
from repertoire import PHRASES
from contacts import SoleContacts
import dance_tools
from rig import HouseRig
from ik_pose import PoseSnapshot
from animation_creation import AnimationCreator
from animation_files import AnimationFileWriter, AnimationTracks, TRACKS_PROPERTY
from animation_export_evaluation import AnimationExportEvaluation

END = 96
BEAT = 12


def smooth(value):
    value = min(1, max(0, value))
    return value * value * (3 - 2 * value)


class HouseAuthor:
    def __init__(self):
        if bpy.app.version[:2] != (5, 2):
            raise RuntimeError('House authoring requires Blender 5.2')
        self.author = HouseRig()
        self.base = self.author.base
        self.soles = SoleContacts()
        bpy.context.scene.render.fps = 24
        bpy.context.scene.render.fps_base = 1
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False
        self.evaluation = AnimationExportEvaluation({bpy.context.scene.objects[rig.name + suffix]
                          for rig in self.author.rigs.values() for suffix in ('', '_deform')})
        self.evaluation.prepare()
        self.output = PROJECT / '.cache/house/candidates'
        self.reports = PROJECT / '.cache/house/authored'
        self.reports.mkdir(parents=True, exist_ok=True)

    def footfalls(self, phrase, actor):
        base = self.base[actor]
        current = {side: Vector(base[side + '_foot']['position']) for side in ('left','right')}
        falls = []
        for beat, offset in enumerate(phrase.steps):
            side = 'left' if beat % 2 == 0 else 'right'
            heading = phrase.turn * math.sin(math.pi * (beat + 1) / 8) ** 2
            if phrase.name in {'swivel', 'charleston', 'loose_legs'}:
                heading += (.25 if beat%4<2 else -.25)
            pitch = 0
            if phrase.name in {'heel_dig', 'toe_touch', 'heel_toe'} and beat<6:
                pitch = -.2 if phrase.name=='heel_dig' or (phrase.name=='heel_toe' and beat%4<2) else .2
            rotation = Quaternion((0,0,1), heading)
            destination = rotation @ (Vector(base[side + '_foot']['position']) + Vector((*offset,0)))
            if pitch:
                pivot = Vector((destination.x, destination.y + (.06 if pitch<0 else -.18), .005))
                destination = pivot + Quaternion((1,0,0),pitch) @ (destination-pivot)
            falls.append((side, current[side].copy(), destination, heading, pitch))
            current[side] = destination
        # Exact neutral closure for both feet at the final two landings.
        if falls:
            for index, side in ((6,'left'),(7,'right')):
                entry = falls[index]
                falls[index] = (side, entry[1], Vector(base[side + '_foot']['position']), 0, 0)
        return falls

    def targets(self, phrase, actor, frame):
        base = self.base[actor]
        time = frame / BEAT
        phase = math.tau * time
        envelope = math.sin(math.pi * frame / END) ** 2
        positions = {side: Vector(base[side+'_foot']['position']) for side in ('left','right')}
        rotations = {side: Quaternion(base[side+'_foot']['rotation']) for side in positions}
        plants = {side: True for side in positions}
        lifts = {side: 0.0 for side in positions}
        for beat, (side, start, destination, heading, pitch) in enumerate(self.footfalls(phrase, actor)):
            fraction = time - beat
            if fraction >= 0:
                amount = smooth((fraction - .125) / .75)
                positions[side] = start.lerp(destination, amount)
                lift = phrase.lift * math.sin(math.pi * amount) ** 2
                positions[side].z += lift
                lifts[side] = lift
                plants[side] = fraction <= .125 or fraction >= .875
                yaw = heading
                previous_yaw = 0 if beat < 2 else self.footfalls(phrase, actor)[beat-2][3]
                previous_pitch = 0 if beat<2 else self.footfalls(phrase,actor)[beat-2][4]
                rotations[side] = Quaternion((0,0,1), previous_yaw + (yaw-previous_yaw)*amount) @ Quaternion((1,0,0),previous_pitch+(pitch-previous_pitch)*amount) @ Quaternion(base[side+'_foot']['rotation'])
        for side in positions:
            positions[side].z = self.soles.retrieve_height(actor, side, rotations[side]) + lifts[side]
        if phrase.name == 'wide_position':
            positions['left'].x += .12
            positions['right'].x -= .12
        if phrase.name == 'staggered_position':
            positions['left'].y -= .15
            positions['right'].y += .15
        heading = phrase.turn * math.sin(math.pi * frame / END) ** 2
        yaw = Quaternion((0,0,1), heading)
        center = (positions['left'] + positions['right']) / 2
        center.z = 0
        for side, other in (('left','right'),('right','left')):
            elevation = positions[side].z - base[side+'_foot']['position'][2]
            weight = min(1, max(0, elevation / max(.001, phrase.lift)))
            center += (positions[other] - positions[side]) * (.3 * weight)
        center.z = 0
        pulse = 0 if phrase.family == 'positions' else .025 * (1 - math.cos(phase))
        sway = (.025 if phrase.name == 'side_jack' else .012) * math.sin(phase/2) * envelope
        torso = Vector(base['torso']['position']) + Vector((center.x+sway,center.y+.015*math.sin(phase)*envelope,-phrase.depth-pulse))
        result = {'torso': {'position': list(torso), 'rotation': list(yaw)},
                  'chest': {'rotation': list(yaw @ Quaternion((1,0,0), .065*math.sin(phase)*envelope))},
                  'hips': {'rotation': list(yaw @ Quaternion((1,0,0), -.045*math.sin(phase-.6)*envelope))},
                  'head': {'rotation': list(yaw @ Quaternion((1,0,0), math.radians(100)))}}
        if phrase.name == 'body_roll':
            result['chest']['rotation'] = list(Quaternion((1,0,0), .12*math.sin(phase)*envelope))
            result['hips']['rotation'] = list(Quaternion((1,0,0), .09*math.sin(phase-1)*envelope))
        for side, sign in (('left',1),('right',-1)):
            result[side+'_foot'] = {'position': list(positions[side]),'rotation':list(rotations[side])}
            knee = yaw @ Vector((sign*.22,-.85,.48)) + Vector((center.x,center.y,0))
            result[side+'_knee'] = {'position':list(knee)}
            arm_swing = 0 if phrase.family == 'positions' else .04*math.sin(phase/2 + sign*.4)*envelope
            hand = yaw @ Vector((sign*(.34+arm_swing),-.18+sign*arm_swing,1.1-phrase.depth*.55)) + Vector((center.x,center.y,0))
            result[side+'_hand'] = {'position':list(hand)}
            result[side+'_elbow'] = {'position':list(yaw @ Vector((sign*.52,.15,1.14-phrase.depth*.4)) + Vector((center.x,center.y,0)))}
        return result, plants

    @staticmethod
    def finish_curves(action, loop=True):
        for layer in action.layers:
            for strip in layer.strips:
                for bag in strip.channelbags:
                    for curve in bag.fcurves:
                        points = curve.keyframe_points
                        if loop and len(points)>1 and points[-1].co.x == END:
                            points[-1].co.y = points[0].co.y
                        if len(points)>1 and max(p.co.y for p in points)-min(p.co.y for p in points)<1e-6:
                            for index in range(len(points)-1,0,-1):
                                points.remove(points[index],fast=True)
                        for point in points:
                            point.interpolation='BEZIER'
                            point.handle_left_type=point.handle_right_type='AUTO_CLAMPED'
                        curve.update()
        action.use_frame_range=True
        action.frame_start=0
        action.frame_end=END

    def configure(self, action, phrase, actor):
        pass

    def create(self, phrase, actor):
        self.author.restore()
        bpy.context.scene.frame_set(0)
        name='house_'+('man' if actor=='player' else 'woman')+'_'+phrase.name
        self.author.controls.rigs = {actor: self.author.rigs[actor]}
        action=AnimationCreator(bpy.context).create(name,{actor.upper()}, {})
        action['House family']=phrase.family
        action['House phrase']=phrase.name
        action['House tempo']=120
        action['House notes']=phrase.description
        action['House reuse']='idle: neutral stance, wrist orientation, relaxed fingers'
        action['animation_loop_end_exclusive'] = phrase.family != 'transitions'
        action['House loop'] = phrase.family != 'transitions'
        action['House provenance'] = 'Original procedural House practice phrase; eight beats at 120 BPM'
        action['House study status'] = 'Procedural study; local review'
        recipe_files = ['author.py', 'rig.py', 'ik_pose.py', 'repertoire.py', 'contacts.py', 'reference.json', 'soles.json']
        if type(self).__name__ == 'FloorAuthor':
            recipe_files.extend(['floor.py', 'floor_fingers_man.json', 'floor_fingers_woman.json'])
        elif type(self).__name__ == 'TransitionAuthor':
            recipe_files.append('transitions.py')
        action['House recipe'] = json.dumps({filename: hashlib.sha256((DIRECTORY / filename).read_bytes()).hexdigest()
                                             for filename in recipe_files}, sort_keys=True)
        self.configure(action, phrase, actor)
        baseline = PoseSnapshot(self.author.controls)
        poses=[]
        frames=sorted(set(range(0,END+1,3)) | {beat*BEAT+offset for beat in range(8) for offset in (1.5,10.5)}) if phrase.steps else (range(0,END+1,3) if phrase.family!='positions' else (0,END))
        for frame in frames:
            targets,_=self.targets(phrase,actor,frame)
            poses.append({'frame':frame,'actors':{actor:targets}})
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                obj.hide_viewport = True
        print('AUTHOR',name,flush=True)
        for pose in poses:
            print('POSE', name, pose['frame'], flush=True)
            # Solve from a complete reference pose while constructing the curves.
            # Sampling happens after all keys and handles have been finalized.
            bpy.context.scene.frame_set(0)
            baseline.restore()
            keyed, measurements = self.author.solve(actor, pose['actors'][actor])
            for bone,path in keyed:
                bone.keyframe_insert(path,frame=pose['frame'],group=bone.name)
        self.finish_curves(action)
        for track in self.author.rigs[actor].animation_data.nla_tracks:
            for strip in track.strips:
                if strip.action == action:
                    strip.action_frame_start, strip.action_frame_end = 0, END
                    strip.frame_start, strip.frame_end = 0, END
        report=self.review(phrase,actor,action)
        (self.reports/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')
        if not report['passed']:
            raise RuntimeError('Motion review failed: '+json.dumps(report))
        action[TRACKS_PROPERTY]=json.dumps(AnimationTracks().retrieve_bindings({action}))
        dance_tools.save_source(action, self.output / 'sources' / (name + '.blend'))
        print('SAVED',name,flush=True)
        return action

    def review(self,phrase,actor,action):
        maximum_plant=0
        minimum_foot_gap=10
        maximum_step=0
        minimum_hand_clearance=10
        minimum_joint_angle=math.pi
        maximum_joint_angle=0
        previous=None
        boundary={}
        frames=sorted(set([i*.5 for i in range(END*2+1)]+[.1,END-.1]))
        for frame in frames:
            bpy.context.scene.frame_set(math.floor(frame),subframe=frame%1)
            targets,plants=self.targets(phrase,actor,frame)
            actual={control:self.author.controls.retrieve_matrix(actor,control) for control in ('left_foot','right_foot','torso','left_hand','right_hand','left_palm','right_palm','head')}
            for side in ('left','right'):
                if plants[side]:
                    maximum_plant=max(maximum_plant,(actual[side+'_foot'].translation-Vector(targets[side+'_foot']['position'])).length)
            for side in ('left','right'):
                if side+'_palm' in targets:
                    maximum_plant=max(maximum_plant,(actual[side+'_palm'].translation-Vector(targets[side+'_palm']['position'])).length)
            minimum_hand_clearance=min(minimum_hand_clearance, *( (actual[side+'_hand'].translation-actual['torso'].translation).length-.25 for side in ('left','right')))
            evaluated=self.author.rigs[actor].evaluated_get(bpy.context.evaluated_depsgraph_get())
            for suffix in ('L','R'):
                for names in (('ORG-thigh.','ORG-shin.','DEF-foot.'),('ORG-upper_arm.','ORG-forearm.','DEF-hand.')):
                    first,joint,last=[evaluated.pose.bones[name+suffix].head for name in names]
                    angle=(first-joint).angle(last-joint)
                    minimum_joint_angle=min(minimum_joint_angle,angle)
                    maximum_joint_angle=max(maximum_joint_angle,angle)
            minimum_foot_gap=min(minimum_foot_gap,(actual['left_foot'].translation-actual['right_foot'].translation).length)
            if previous:
                maximum_step=max(maximum_step,max((matrix.translation-previous[key].translation).length for key,matrix in actual.items()))
            previous=actual
            if frame in (0,.1,END-.1,END):
                boundary[frame]=actual
        endpoint=max((boundary[0][key].translation-boundary[END][key].translation).length for key in boundary[0])
        velocity=max(((boundary[.1][key].translation-boundary[0][key].translation)/.1-(boundary[END][key].translation-boundary[END-.1][key].translation)/.1).length*24 for key in boundary[0])
        orientation=max(min(boundary[0][key].to_quaternion().rotation_difference(boundary[END][key].to_quaternion()).angle, abs(math.tau-boundary[0][key].to_quaternion().rotation_difference(boundary[END][key].to_quaternion()).angle)) for key in boundary[0])
        return {'minimum_hand_torso_proxy_clearance':minimum_hand_clearance,'joint_angle_range': [minimum_joint_angle,maximum_joint_angle],'loop_orientation_error':orientation,'animation':action.name,'blender':bpy.app.version_string,'samples':len(frames),'plant_error':maximum_plant,'minimum_ankle_separation':minimum_foot_gap,'maximum_half_frame_displacement':maximum_step,'loop_position_error':endpoint,'loop_velocity_error':velocity,'passed':minimum_hand_clearance>.025 and minimum_joint_angle>.25 and maximum_joint_angle<3.13 and orientation<.01 and maximum_plant<.003 and minimum_foot_gap>.15 and maximum_step<.12 and endpoint<.003 and velocity<.1}

    def run(self,names):
        try:
            for phrase in PHRASES:
                if not names or phrase.name in names:
                    for actor in ('player','partner'):
                        self.create(phrase,actor)
        finally:
            self.evaluation.restore()


if __name__=='__main__':
    HouseAuthor().run(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
