"""Fresh-process source, native bake, contacts, skin, and loop review for a House clip."""
import hashlib
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace

import bpy
import numpy as np
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

ROOT = Path(__file__).resolve().parents[2]
for directory in (ROOT / 'scripts', Path(__file__).resolve().parent):
    sys.path.insert(0, str(directory))
import dance_tools
from track_chooser import TrackChooser
from animation_export_evaluation import AnimationExportEvaluation
from wardrobe import apply_profile
from author import HouseAuthor
from floor import FloorAuthor
from transitions import TransitionAuthor
from turns import HeadingAuthor, TurnAuthor
from foot_accents import FootAccentAuthor
from contacts import SoleContacts
from ik_pose import RigControls
from repertoire import CATALOG


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def retrieve_matrices(rig):
    evaluated = rig.evaluated_get(bpy.context.evaluated_depsgraph_get())
    return np.array([np.array(evaluated.matrix_world @ bone.matrix) for bone in evaluated.pose.bones])


class SkinReview:
    """Evaluated base-body surfaces with the native subdivision and helper mask."""
    def __init__(self, actor):
        self.body = bpy.context.scene.objects[actor.capitalize() + '.body']
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH' and obj != self.body:
                obj.hide_viewport = True
        self.body.hide_viewport = False
        self.body.hide_set(False)
        apply_profile('base')
        self.groups = {group.index: group.name for group in self.body.vertex_groups}
        self.minimum = float('inf')
        self.maximum_support_gap = 0.0
        self.maximum_hand_gap = 0.0
        self.minimum_finger = float('inf')
        self.maximum_lowest = -float('inf')
        self.collisions = []
        self.indices = None
        self.patches = None

    @staticmethod
    def region(name):
        for side in 'LR':
            if name.endswith('.' + side) or '.' + side + '.' in name:
                for prefix, region in [('foot', 'foot'), ('toe', 'foot'), ('shin', 'shin'),
                                       ('thigh', 'thigh'), ('forearm', 'arm'), ('upper_arm', 'upper_arm'),
                                       ('hand', 'hand'), ('palm', 'hand'), ('f_', 'finger'), ('thumb', 'finger')]:
                    if name.startswith('DEF-' + prefix):
                        return region + '.' + side
        return 'torso' if name.startswith(('DEF-spine', 'DEF-pelvis', 'DEF-breast', 'DEF-shoulder')) else 'other'

    def sample(self, frame, plants, floor, collisions):
        evaluated = self.body.evaluated_get(bpy.context.evaluated_depsgraph_get())
        mesh = evaluated.to_mesh()
        coordinates = np.empty(len(mesh.vertices) * 3)
        mesh.vertices.foreach_get('co', coordinates)
        transform = np.array(evaluated.matrix_world)
        points = coordinates.reshape((-1, 3)) @ transform[:3, :3].T + transform[:3, 3]
        if self.indices is None:
            labels = [self.region(max(((weight.weight, self.groups[weight.group])
                       for weight in vertex.groups if self.groups[weight.group].startswith('DEF-')),
                      default=(0, 'other'))[1]) for vertex in mesh.vertices]
            self.indices = {region: np.array([index for index, label in enumerate(labels) if label == region])
                            for region in set(labels)}
            self.patches = {region: [tuple(polygon.vertices) for polygon in mesh.polygons
                            if all(labels[index] == region for index in polygon.vertices)] for region in set(labels)}
        lowest = float(points[:, 2].min())
        self.minimum = min(self.minimum, lowest)
        self.maximum_lowest = max(self.maximum_lowest, lowest)
        for side, suffix in [('left', 'L'), ('right', 'R')]:
            if plants[side]:
                height = float(points[self.indices['foot.' + suffix], 2].min())
                self.maximum_support_gap = max(self.maximum_support_gap, abs(height))
            if floor:
                self.maximum_hand_gap = max(self.maximum_hand_gap, abs(float(points[self.indices['hand.' + suffix], 2].min())))
                self.minimum_finger = min(self.minimum_finger, float(points[self.indices['finger.' + suffix], 2].min()))
        if collisions:
            pairs = [(a + '.L', b + '.R') for a in ('thigh', 'shin', 'foot') for b in ('thigh', 'shin', 'foot')]
            pairs += [(part + '.' + side, 'torso') for part in ('arm', 'hand') for side in 'LR']
            trees = {}
            bounds = {name: (points[indices].min(axis=0), points[indices].max(axis=0))
                      for name, indices in self.indices.items() if len(indices)}
            for first, second in pairs:
                if first in bounds and second in bounds and self.patches[first] and self.patches[second]:
                    first_minimum, first_maximum = bounds[first]
                    second_minimum, second_maximum = bounds[second]
                    if np.all(first_maximum >= second_minimum) and np.all(second_maximum >= first_minimum):
                        for name in (first, second):
                            if name not in trees:
                                trees[name] = BVHTree.FromPolygons(points.tolist(), self.patches[name])
                        overlaps = trees[first].overlap(trees[second])
                        if overlaps:
                            self.collisions.append(dict(frame=frame, regions=[first, second], triangles=len(overlaps)))
        evaluated.to_mesh_clear()

    def retrieve_report(self, count, floor):
        return dict(samples=count, units='meters', minimumHeight=self.minimum,
                    maximumLowestHeight=self.maximum_lowest, maximumSupportGap=self.maximum_support_gap,
                    maximumPalmGap=self.maximum_hand_gap if floor else None,
                    minimumFingerHeight=self.minimum_finger if floor else None,
                    surfaceCrossings=self.collisions,
                    collisionCoverage='Opposite legs and feet; forearms and palms against torso at authored keys and six-frame intervals')


def main():
    name = sys.argv[sys.argv.index('--') + 1]
    actor, move = name.removeprefix('house_').split('_', 1)
    role = {'man': 'player', 'woman': 'partner'}[actor]
    phrase, module = next((phrase, module) for phrase, module in CATALOG if phrase.name == move)
    source = ROOT / '.cache/house/candidates/sources' / (name + '.blend')
    output = ROOT / '.cache/house/validated' / (name + '.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(source))
    dance_tools.register()
    scene = bpy.context.scene
    TrackChooser(scene).apply(name)
    action = bpy.data.actions[name]
    baked = bpy.data.actions[name + '.baked']
    assert tuple(action.frame_range) == (0, 96)
    assert scene.render.fps / scene.render.fps_base == 24
    assert scene.frame_end == (96 if module == 'transitions' else 95)
    assert action['player_asset_participants'] == role.upper()
    assert all(not library.is_missing for library in bpy.data.libraries)
    control = scene.objects[actor.capitalize() + '.rigify']
    rig = scene.objects[actor.capitalize() + '.rigify_deform']
    for obj in (control, rig):
        obj.hide_viewport = False
        obj.hide_set(False)
    for bone in rig.pose.bones:
        bone.matrix_basis = Matrix.Identity(4)
        for constraint in bone.constraints:
            constraint.mute = False
    rig.animation_data.action = None
    for track in rig.animation_data.nla_tracks:
        track.mute = True
    recipe_class = TurnAuthor if move == 'half_turn_return' else {
        'author': HouseAuthor, 'floor': FloorAuthor, 'transitions': TransitionAuthor}[module]
    if actor == 'woman' and move in ('heel_toe', 'toe_touch'):
        recipe_class = FootAccentAuthor
    elif move in ('quarter_turn_left', 'quarter_turn_right'):
        recipe_class = HeadingAuthor
    recipe = recipe_class.__new__(recipe_class)
    reference = json.loads(Path(__file__).with_name('reference.json').read_text())
    recipe.base = {key: value['targets'] for key, value in reference['actors'].items()}
    if isinstance(recipe, TurnAuthor):
        recipe.prepare_base(recipe.base)
    recipe.soles = SoleContacts()
    recipe.author = SimpleNamespace(rigs={role: control}, controls=RigControls(bpy.context, {role: control}))
    evaluation = AnimationExportEvaluation({control, rig})
    evaluation.prepare()
    authored = recipe.review(phrase, role, action)
    evaluation.restore()
    skin = SkinReview(actor)
    key_frames = {float(point.co.x) for layer in action.layers for strip in layer.strips
                  for bag in strip.channelbags for curve in bag.fcurves for point in curve.keyframe_points}
    frames = sorted(set(i / 4 for i in range(385)) | key_frames | {.1, 95.9})
    surface_samples = 0
    native = []
    for frame in frames:
        scene.frame_set(math.floor(frame), subframe=frame % 1)
        matrices = retrieve_matrices(rig)
        assert np.isfinite(matrices).all()
        native.append(matrices)
        _, plants = recipe.targets(phrase, role, frame)
        if (frame * 2).is_integer() or frame in key_frames or frame in (.1, 95.9):
            skin.sample(frame, plants, module == 'floor', frame in key_frames or frame % 6 == 0)
            surface_samples += 1
    skin_report = skin.retrieve_report(surface_samples, module == 'floor')
    boundaries = {frame: native[frames.index(frame)] for frame in (0, .1, 95.9, 96)}
    seam_position = float(np.linalg.norm(boundaries[96][:, :3, 3] - boundaries[0][:, :3, 3], axis=1).max())
    seam_velocity = float(np.linalg.norm((boundaries[.1][:, :3, 3] - boundaries[0][:, :3, 3]
                          - boundaries[96][:, :3, 3] + boundaries[95.9][:, :3, 3]) * 240, axis=1).max())
    reference_output = ROOT / '.cache/house/runtime-reference' / (name + '.json')
    reference_output.parent.mkdir(parents=True, exist_ok=True)
    positions = np.array(native)[:, :, :3, 3][:, :, [0, 2, 1]]
    positions[:, :, 2] *= -1
    reference_output.write_text(json.dumps(dict(id=name, sourceSha256=digest(source), frames=frames,
        bones=[bone.name.replace('.', '') for bone in rig.pose.bones],
        positions=np.round(positions, 8).tolist()), separators=(',', ':')))
    evaluation.prepare()
    rig.animation_data.use_nla = False
    rig.animation_data.action = baked
    rig.animation_data.action_slot = next(slot for slot in baked.slots if slot.identifier == 'OB' + rig.name)
    for bone in rig.pose.bones:
        for constraint in bone.constraints:
            constraint.mute = True
    maximum_integer = maximum_fractional = maximum_position = maximum_rotation = 0.0
    worst = None
    for frame, expected in zip(frames, native):
        scene.frame_set(math.floor(frame), subframe=frame % 1)
        actual = retrieve_matrices(rig)
        assert np.isfinite(actual).all()
        error = float(np.abs(actual - expected).max())
        if frame.is_integer(): maximum_integer = max(maximum_integer, error)
        else: maximum_fractional = max(maximum_fractional, error)
        position = float(np.linalg.norm(actual[:, :3, 3] - expected[:, :3, 3], axis=1).max())
        if position > maximum_position:
            maximum_position, worst = position, frame
        for first, second in zip(actual, expected):
            angle = Matrix(first.tolist()).to_quaternion().rotation_difference(Matrix(second.tolist()).to_quaternion()).angle
            maximum_rotation = max(maximum_rotation, min(angle, abs(math.tau-angle)))
    evaluation.restore()
    surface_passed = (skin.minimum >= -.004 and skin.maximum_support_gap <= .012
                      and skin.maximum_lowest <= .015 and not skin.collisions)
    passed = (authored['passed'] and maximum_integer < .0001 and maximum_position < .005
              and maximum_rotation < .06 and surface_passed)
    dependencies = {str(Path(bpy.path.abspath(library.filepath)).resolve().relative_to(ROOT)):
                    digest(Path(bpy.path.abspath(library.filepath))) for library in bpy.data.libraries}
    dependencies['animations/shared_scene_data.blend'] = digest(ROOT / 'animations/shared_scene_data.blend')
    report = dict(id=name, passed=passed, sourceSha256=digest(source),
                  exportSha256=digest(source.parent.parent / (name + '.glb')),
                  dependencySha256=dependencies, blender=bpy.app.version_string, frames=frames,
                  role=role.upper(), slots=[slot.identifier for slot in action.slots],
                  sourceRange=list(action.frame_range), playbackRange=[scene.frame_start,scene.frame_end],
                  effectiveFrameRate=24, authoredControls=authored, skin=skin_report,
                  sourceSeam=dict(loop=module != 'transitions', positionError=seam_position,
                                  velocityError=seam_velocity, velocityUnits='meters per second'),
                  recipeSha256=json.loads(action['House recipe']) if 'House recipe' in action else {},
                  bake=dict(bones=len(rig.pose.bones), maximumIntegerMatrixError=maximum_integer,
                            maximumFractionalMatrixError=maximum_fractional,
                            maximumPositionError=maximum_position, maximumAngularError=maximum_rotation,
                            worstPositionFrame=worst, liveFollowConstraints='muted'),
                  tolerances=dict(integerMatrix=.0001, position=.005, angle=.06,
                                  penetration=.004, supportGap=.012, lowestSurface=.015),
                  visualReview='pending', studyStatus='Procedural study')
    output.write_text(json.dumps(report, indent=2)+'\n')
    print('REVIEW', name, passed, authored['passed'], skin_report, report['bake'], flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
