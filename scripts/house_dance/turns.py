"""Maintain quaternion continuity through the half-turn's 180-degree heading."""
import hashlib
import json
import math
from pathlib import Path

from mathutils import Quaternion, Vector

from author import HouseAuthor


class TurnRig:
    def __init__(self, author, actor):
        import bpy
        self.author = author
        self.rigs, self.controls, self.solver = author.rigs, author.controls, author.solver

    def solve(self, actor, specifications):
        import bpy
        keyed, measurements = self.author.solve(actor, specifications)
        rig = self.rigs[actor]
        hands = {}
        for side, suffix in (('left', 'L'), ('right', 'R')):
            # Use the native anatomical wrist frame. A constrained initial
            # hand offset can sit on a limit and flip its Euler branch as the
            # torso turns through 90 degrees.
            wrist = rig.pose.bones['hand_tweak.' + suffix]
            reference = wrist.constraints['Natural Wrist Rotation'].space_object
            graph = bpy.context.evaluated_depsgraph_get()
            orientation = reference.evaluated_get(graph).matrix_world.to_quaternion()
            hand = rig.pose.bones['hand_ik.' + suffix]
            matrix = (rig.matrix_world.inverted().to_quaternion() @ orientation).to_matrix().to_4x4()
            matrix.translation = hand.matrix.translation
            hand.matrix = matrix
            self.controls.update()
            hands[side + '_hand'] = dict(position=specifications[side + '_hand']['position'])
        hand_keys, hand_measurements = self.author.solve(actor, hands)
        return keyed | hand_keys, measurements + hand_measurements


class HeadingAuthor(HouseAuthor):
    def targets(self, phrase, actor, frame):
        targets, plants = super().targets(phrase, actor, frame)
        heading = Quaternion((0, 0, 1), phrase.turn * math.sin(math.pi * frame / 96) ** 2)
        targets['root'] = dict(rotation=list(heading))
        return targets, plants

    def configure(self, action, phrase, actor):
        recipe = json.loads(action['House recipe'])
        recipe['turns.py'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        action['House recipe'] = json.dumps(recipe, sort_keys=True)


class TurnAuthor(HeadingAuthor):
    def __init__(self):
        super().__init__()
        self.prepare_base(self.base)

    def create(self, phrase, actor):
        import bpy
        import dance_tools
        from animation_export_evaluation import AnimationExportEvaluation
        from track_chooser import TrackChooser
        action = super().create(phrase, actor)
        name = action.name
        self.evaluation.restore()
        source = self.output / 'sources' / (name + '.blend')
        bpy.ops.wm.open_mainfile(filepath=str(source))
        dance_tools.register()
        TrackChooser(bpy.context.scene).apply(name)
        action = bpy.data.actions[name]
        rig = bpy.context.scene.objects[name.split('_')[1].capitalize() + '.rigify']
        rig.animation_data.action = action
        rig.animation_data.action_slot = next(slot for slot in action.slots if slot.identifier == 'OB' + rig.name)
        rig.animation_data.use_nla = False
        evaluation = AnimationExportEvaluation({rig, bpy.context.scene.objects[rig.name + '_deform']})
        evaluation.prepare()
        try:
            # Portable sources recreate anatomical frames from their shared
            # template. Fit the wrist keys against that freshly composed rig.
            self.finish_curves(action)
            dance_tools.save_source(action, source)
        finally:
            evaluation.restore()
        return action

    @staticmethod
    def prepare_base(actors):
        for base in actors.values():
            base['left_foot']['position'][0] += .14
            base['right_foot']['position'][0] -= .14

    def targets(self, phrase, actor, frame):
        targets, plants = super().targets(phrase, actor, frame)
        heading = Quaternion((0, 0, 1), phrase.turn * math.sin(math.pi * frame / 96) ** 2)
        for side, sign in (('left', 1), ('right', -1)):
            for control, offset in (('hand', (sign * .09, -.07, .10)),
                                    ('elbow', (sign * .08, -.20, .03)),
                                    ('knee', (sign * .14, 0, 0))):
                targets[side + '_' + control]['position'] = list(Vector(targets[side + '_' + control]['position'])
                                                                 + heading @ Vector(offset))
        return targets, plants

    def configure(self, action, phrase, actor):
        recipe = json.loads(action['House recipe'])
        recipe['turns.py'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        action['House recipe'] = json.dumps(recipe, sort_keys=True)
        targets, _ = self.targets(phrase, actor, 0)
        keyed, _ = self.author.solve(actor, targets)
        for bone, path in keyed:
            bone.keyframe_insert(path, frame=0, group=bone.name)
        self.author = TurnRig(self.author, actor)
    def review(self, phrase, actor, action):
        import bpy
        import dance_tools
        report = super().review(phrase, actor, action)
        previous = None
        worst = (0, None, None)
        for index in range(193):
            frame = index / 2
            bpy.context.scene.frame_set(int(frame), subframe=frame % 1)
            actual = {name: self.author.controls.retrieve_matrix(actor, name).translation.copy()
                      for name in ('left_foot', 'right_foot', 'torso', 'left_hand', 'right_hand', 'left_palm', 'right_palm', 'head')}
            if previous:
                for name, position in actual.items():
                    distance = (position - previous[name]).length
                    if distance > worst[0]:
                        worst = (distance, name, frame)
            previous = actual
        report['worst_displacement'] = worst
        if not report['passed']:
            dance_tools.save_source(action, Path(__file__).resolve().parents[2] / '.cache/house/debug/sources' / (action.name + '.blend'))
        return report

    def finish_curves(self, action, loop=True):
        import bpy
        from ik_pose import PoseSolver, PoseTarget, RigControls
        from repertoire import CATALOG
        HouseAuthor.finish_curves(action, loop)
        actor = action.name.split('_')[1].capitalize()
        rig = bpy.context.scene.objects[actor + '.rigify']
        role = 'player' if actor == 'Man' else 'partner'
        phrase = next(phrase for phrase, _module in CATALOG if phrase.name == 'half_turn_return')
        controls = RigControls(bpy.context, {role: rig})
        solver = PoseSolver(controls, tolerance=.0005)
        # Root turning curves need intermediate foot keys to hold the same
        # world-space support point between the sparse body poses.
        contact_frames = {index * 1.5 for index in range(65)}
        contact_frames.update(beat * 12 + offset for beat in range(8) for offset in (.5, 1, 11, 11.5))
        for frame in sorted(contact_frames):
            bpy.context.scene.frame_set(int(frame), subframe=frame % 1)
            targets, _plants = self.targets(phrase, role, frame)
            keyed, _measurements = solver.solve([PoseTarget(controls, role, side + '_foot', targets[side + '_foot'])
                                                 for side in ('left', 'right')])
            for bone, path in keyed:
                bone.keyframe_insert(path, frame=frame, group=bone.name)
        HouseAuthor.finish_curves(action, loop)
        frames = sorted({float(point.co.x) for layer in action.layers for strip in layer.strips
                         for bag in strip.channelbags for curve in bag.fcurves
                         if 'hand_ik.' in curve.data_path for point in curve.keyframe_points})
        # Sample complete parent curves before setting wrist orientation.
        # During sparse construction the torso is still evaluated at frame zero.
        for frame in frames:
            bpy.context.scene.frame_set(int(frame), subframe=frame % 1)
            for suffix in ('L', 'R'):
                hand = rig.pose.bones['hand_ik.' + suffix]
                wrist = rig.pose.bones['hand_tweak.' + suffix]
                reference = wrist.constraints['Natural Wrist Rotation'].space_object
                graph = bpy.context.evaluated_depsgraph_get()
                orientation = reference.evaluated_get(graph).matrix_world.to_quaternion()
                matrix = (rig.matrix_world.inverted().to_quaternion() @ orientation).to_matrix().to_4x4()
                matrix.translation = hand.matrix.translation
                hand.matrix = matrix
                rig.update_tag()
                bpy.context.view_layer.update()
                hand.keyframe_insert('rotation_quaternion', frame=frame, group=hand.name)
        for layer in action.layers:
            for strip in layer.strips:
                for bag in strip.channelbags:
                    rotations = {}
                    for curve in bag.fcurves:
                        if curve.data_path.endswith('rotation_quaternion'):
                            rotations.setdefault(curve.data_path, {})[curve.array_index] = curve
                    for components in rotations.values():
                        if len(components) == 4:
                            points = [{point.co.x: point for point in components[index].keyframe_points}
                                      for index in range(4)]
                            frames = sorted(set.intersection(*(set(component) for component in points)))
                            previous = None
                            for frame in frames:
                                rotation = Quaternion([component[frame].co.y for component in points]).normalized()
                                if previous and rotation.dot(previous) < 0:
                                    rotation.negate()
                                for index, component in enumerate(points):
                                    component[frame].co.y = rotation[index]
                                previous = rotation
        HouseAuthor.finish_curves(action, loop)
