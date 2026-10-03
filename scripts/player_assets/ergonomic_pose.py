"""Fit the current Rigify poses together around nearby gravity supports."""

from dataclasses import dataclass
import math

import bpy
import numpy as np
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

from ergonomic_support import SupportEquilibrium
from ergonomic_collisions import ArmBodyCollisions


@dataclass
class ErgonomicSettings:
    """Distances use Blender world units; angular bounds use radians."""

    floor: float = 0.0
    proximity: float = 0.06
    translation: float = 0.08
    rotation: float = math.radians(10)
    iterations: int = 6


class SurfaceAnchor:
    def __init__(self, rig, bone, position):
        self.rig = rig
        self.bone = bone
        frame = rig.matrix_world @ rig.pose.bones[bone].matrix
        self.local = frame.inverted() @ Vector(position)
        self.orientation = frame.to_quaternion().inverted()

    def retrieve_position(self):
        return self.rig.matrix_world @ self.rig.pose.bones[self.bone].matrix @ self.local

    def retrieve_direction(self, direction):
        frame = self.rig.matrix_world @ self.rig.pose.bones[self.bone].matrix
        return frame.to_quaternion() @ self.orientation @ direction


class BodySurface:
    """Capture the displayed skin surface and bind samples to its deform bones."""

    def __init__(self, context, rig):
        self.rig = rig
        self.object = self.retrieve_body(context, rig)
        evaluated = self.object.evaluated_get(context.evaluated_depsgraph_get())
        mesh = evaluated.data
        names = {group.index: group.name for group in self.object.vertex_groups
                 if group.name.startswith('DEF-') and group.name in rig.pose.bones}
        positions = [evaluated.matrix_world @ vertex.co for vertex in mesh.vertices]
        self.bones = []
        for vertex in mesh.vertices:
            weights = [(weight.weight, names[weight.group]) for weight in vertex.groups
                       if weight.group in names]
            self.bones.append(max(weights)[1] if weights else 'DEF-spine')
        polygons = [tuple(polygon.vertices) for polygon in mesh.polygons]
        self.tree = BVHTree.FromPolygons(positions, polygons)
        self.polygons = polygons
        # Sparse meshes benefit from contact points inside their flat faces.
        if len(polygons) < 10000:
            for polygon in polygons:
                positions.append(sum((positions[index] for index in polygon), Vector()) / len(polygon))
                self.bones.append(self.bones[polygon[0]])
        self.positions = positions
        regions = {}
        for index, bone in enumerate(self.bones):
            regions.setdefault(self.retrieve_region(bone), []).append(index)
        self.regions = {}
        for region, indices in regions.items():
            # Preserve surface extremes and a distributed set for contact discovery.
            samples = set(indices[::max(1, len(indices) // 12)])
            for axis in range(3):
                samples.add(min(indices, key=lambda index: positions[index][axis]))
                samples.add(max(indices, key=lambda index: positions[index][axis]))
            self.regions[region] = [SurfaceAnchor(rig, self.bones[index], positions[index])
                                    for index in sorted(samples)]

    @staticmethod
    def retrieve_body(context, rig):
        graph = context.evaluated_depsgraph_get()
        targets = {rig.name, rig.name + '_deform'}
        landmarks = {'DEF-spine', 'DEF-spine.006', 'DEF-hand.L', 'DEF-hand.R',
                     'DEF-foot.L', 'DEF-foot.R'}
        candidates = []
        for obj in context.scene.objects:
            if obj.type == 'MESH' and obj.visible_get(view_layer=context.view_layer) and not obj.hide_render:
                bound = any(modifier.type == 'ARMATURE' and modifier.object
                            and modifier.object.name in targets for modifier in obj.modifiers)
                if bound:
                    mesh = obj.evaluated_get(graph).data
                    if mesh.polygons:
                        coverage = len(landmarks.intersection(obj.vertex_groups.keys()))
                        candidates.append((coverage, len(mesh.vertices), obj.name, obj))
        if candidates:
            return max(candidates, key=lambda item: item[:3])[3]
        else:
            raise ValueError(f'Show the rendered body surface for {rig.name} before adjusting its pose')

    def retrieve_region(self, bone):
        for side in ('L', 'R'):
            if bone.endswith('.' + side) or '.' + side + '.' in bone:
                if any(part in bone for part in ('hand', 'palm', 'f_', 'thumb')):
                    return 'hand.' + side
                if any(part in bone for part in ('foot', 'toe')):
                    return 'foot.' + side
                if 'shin' in bone or 'knee' in bone:
                    return 'knee.' + side
                for part in ('thigh', 'upper_arm', 'forearm'):
                    if part in bone:
                        return part + '.' + side
        head = self.rig.data.bones.get('DEF-spine.006')
        if head and self.rig.data.bones[bone].head_local.z >= head.head_local.z - .02:
            return 'head'
        return bone

    def retrieve_nearest(self, position):
        nearest, normal, polygon, distance = self.tree.find_nearest(position)
        index = min(self.polygons[polygon], key=lambda index: (self.positions[index] - nearest).length)
        return SurfaceAnchor(self.rig, self.bones[index], nearest), normal, distance


class PoseVariables:
    """Bounded control changes, with existing IK modes and control locks preserved."""

    def __init__(self, rigs, settings):
        self.controls = []
        self.parameters = []
        self.bounds = []
        for rig in rigs:
            names = [('root', False, False), ('torso', True, False), ('hips', False, True),
                     ('chest', False, True), ('head', False, True)]
            for side in ('L', 'R'):
                for limb, parent in (('hand', 'upper_arm'), ('foot', 'thigh')):
                    settings_bone = rig.pose.bones.get(f'{parent}_parent.{side}')
                    if settings_bone and settings_bone.get('IK_FK', 0) < 0.001:
                        names.append((f'{limb}_ik.{side}', True, True))
                        if limb == 'hand':
                            pole = settings_bone.get('pole_vector', False)
                            names.append((f'upper_arm_ik_target.{side}' if pole else f'upper_arm_ik.{side}',
                                          bool(pole), not pole))
                    elif settings_bone and settings_bone.get('IK_FK', 0) > .999:
                        chain = ('upper_arm_fk', 'forearm_fk', 'hand_fk') if limb == 'hand' else (
                            'thigh_fk', 'shin_fk', 'foot_fk')
                        names.extend((f'{control}.{side}', False, True) for control in chain)
            for name, translate, rotate in names:
                bone = rig.pose.bones.get(name)
                if bone:
                    control = len(self.controls)
                    self.controls.append((bone, bone.matrix_basis.copy()))
                    for mode, enabled, locks, bound in (
                            ('location', translate, bone.lock_location, settings.translation),
                            ('rotation', rotate, bone.lock_rotation, settings.rotation)):
                        for axis in range(3):
                            if enabled and not locks[axis]:
                                self.parameters.append((control, mode, axis))
                                # Local translations are scaled into world distance.
                                scale = (rig.matrix_world @ bone.matrix).to_scale()[axis]
                                self.bounds.append(bound / max(abs(scale), 1e-6) if mode == 'location' else bound)
        self.bounds = np.asarray(self.bounds)

    def apply(self, values):
        translations = [Vector((0, 0, 0)) for _entry in self.controls]
        rotations = [Vector((0, 0, 0)) for _entry in self.controls]
        for value, (index, mode, axis) in zip(values, self.parameters):
            (translations if mode == 'location' else rotations)[index][axis] = value
        for (bone, basis), translation, rotation in zip(self.controls, translations, rotations):
            matrix = basis.copy()
            for axis in range(3):
                matrix = matrix @ Matrix.Rotation(rotation[axis], 4, 'XYZ'[axis])
            matrix.translation = basis.translation + translation
            bone.matrix_basis = matrix

    def restore(self):
        for bone, basis in self.controls:
            bone.matrix_basis = basis

    def keyframe(self):
        for bone, basis in self.controls:
            if max(abs(bone.matrix_basis[row][column] - basis[row][column])
                   for row in range(4) for column in range(4)) > 1e-6:
                rotation = ('rotation_quaternion' if bone.rotation_mode == 'QUATERNION' else
                            'rotation_axis_angle' if bone.rotation_mode == 'AXIS_ANGLE' else 'rotation_euler')
                for path in ('location', rotation):
                    bone.keyframe_insert(path, group=bone.name)


class FloorPlacement:
    """Settle each touching participant group using the final evaluated skin."""

    def __init__(self, solver):
        self.solver = solver

    def retrieve_minimum(self, participants):
        graph = self.solver.context.evaluated_depsgraph_get()
        minimum = math.inf
        for participant in participants:
            surface = self.solver.surfaces[participant]
            body = surface.object.evaluated_get(graph)
            minimum = min(minimum, min((body.matrix_world @ vertex.co).z for vertex in body.data.vertices))
        return minimum

    def apply(self):
        groups = [{index} for index in range(len(self.solver.rigs))]
        for source, target, *_contact in self.solver.pair_contacts:
            first = next(group for group in groups if source in group)
            second = next(group for group in groups if target in group)
            if first is not second:
                first.update(second)
                groups.remove(second)
        grounded = {participant for participant, _sample in self.solver.floor_contacts}
        adjustments = []
        for group in groups:
            if group.intersection(grounded):
                distance = self.solver.settings.floor + .0005 - self.retrieve_minimum(group)
                if abs(distance) > self.solver.settings.translation:
                    raise ValueError('Increase Maximum movement to reach the floor with the displayed skin')
                previous = []
                for participant in sorted(group):
                    rig = self.solver.rigs[participant]
                    control = rig.pose.bones.get('root') or rig.pose.bones.get('torso')
                    if control is None:
                        raise ValueError(f'Provide a placement control for {rig.name}')
                    previous.append((rig, control, control.location.copy(),
                                     {bone.name: rig.matrix_world @ bone.head for bone in rig.pose.bones
                                      if bone.name.startswith('DEF-')}))
                    world = rig.matrix_world @ control.matrix
                    world.translation.z += distance
                    control.matrix = rig.matrix_world.inverted() @ world
                self.solver.update()
                for rig, control, location, positions in previous:
                    basis = next(basis for bone, basis in self.solver.variables.controls if bone == control)
                    scale = (rig.matrix_world @ control.matrix).to_scale()
                    if any(abs(control.location[axis] - basis.translation[axis]) * abs(scale[axis])
                           > self.solver.settings.translation + 1e-6 for axis in range(3)):
                        raise ValueError('Increase Maximum movement to reach the floor with the displayed skin')
                    if any(locked and abs(control.location[axis] - location[axis]) > 1e-6
                           for axis, locked in enumerate(control.lock_location)):
                        raise ValueError(f'Allow vertical placement on {rig.name} to reach the floor')
                    expected = Vector((0, 0, distance))
                    if any((rig.matrix_world @ rig.pose.bones[name].head - point - expected).length > .0001
                           for name, point in positions.items()):
                        raise ValueError(f'Use root-following controls on {rig.name} to preserve contacts during floor placement')
                floor_gap = self.retrieve_minimum(group) - self.solver.settings.floor
                if abs(floor_gap - .0005) > .001:
                    raise ValueError('Floor placement requires root-following skin and constraints')
                adjustments.append(distance)
        return adjustments


class ErgonomicPose:
    """One objective and one parameter vector for every animation participant."""

    def __init__(self, context, rigs, settings=None):
        self.context = context
        self.rigs = list(rigs)
        self.settings = settings or ErgonomicSettings()
        if not self.rigs:
            raise ValueError('Choose an animation with character participants')
        self.variables = PoseVariables(self.rigs, self.settings)
        self.update()
        self.surfaces = [BodySurface(context, rig) for rig in self.rigs]
        self.floor_contacts = []
        self.pair_contacts = []
        self.collision_pairs = []
        self.samples = [sample for surface in self.surfaces for region in surface.regions.values()
                        for sample in region]
        self.original = np.array([sample.retrieve_position() for sample in self.samples])
        self.capture_contacts()
        self.self_collisions = ArmBodyCollisions(self.surfaces, self.settings.proximity + self.settings.translation * 2)
        self.equilibrium = SupportEquilibrium()

    def update(self):
        for rig in self.rigs:
            rig.update_tag()
        self.context.view_layer.update()

    @classmethod
    def retrieve_participants(cls, context):
        from animation_creation import AnimationCreator
        from animation_participants import retrieve_active_action, includes
        action = retrieve_active_action(context)
        return [context.scene.objects[name] for role, name in AnimationCreator.RIGS.items()
                if includes(action, role) and name in context.scene.objects
                and context.scene.objects[name].is_editable]

    def capture_contacts(self):
        for participant, surface in enumerate(self.surfaces):
            for samples in surface.regions.values():
                lowest = min(sample.retrieve_position().z for sample in samples)
                if abs(lowest - self.settings.floor) <= self.settings.proximity:
                    nearby = [sample for sample in samples if sample.retrieve_position().z <= lowest + 0.015]
                    chosen = {min(nearby, key=lambda sample: sample.retrieve_position().z)}
                    for axis in (0, 1):
                        chosen.add(min(nearby, key=lambda sample: sample.retrieve_position()[axis]))
                        chosen.add(max(nearby, key=lambda sample: sample.retrieve_position()[axis]))
                    self.floor_contacts.extend((participant, sample) for sample in chosen)
        for first, surface in enumerate(self.surfaces):
            for second in range(first + 1, len(self.surfaces)):
                # Both directions capture a small hand resting on a larger body surface.
                for source, target in ((first, second), (second, first)):
                    for samples in self.surfaces[source].regions.values():
                        candidates = []
                        for sample in samples:
                            anchor, normal, distance = self.surfaces[target].retrieve_nearest(sample.retrieve_position())
                            if distance <= self.settings.proximity + self.settings.translation * 2:
                                candidates.append((distance, sample, anchor, normal))
                        candidates.sort(key=lambda item: (item[0] > self.settings.proximity,
                                                          abs(item[3].z) < .35, item[0]))
                        for distance, sample, anchor, normal in candidates[:2]:
                            difference = sample.retrieve_position() - anchor.retrieve_position()
                            self.collision_pairs.append((sample, anchor, normal, min(0, difference.dot(normal))))
                            if distance <= self.settings.proximity:
                                # An upward normal represents gravity support; side contacts retain their gap.
                                supporting = ((1 if normal.z > 0 else -1)
                                              if abs(normal.z) > .35 and difference.dot(normal) >= -.015 else 0)
                                self.pair_contacts.append((source, target, sample, anchor, normal,
                                                           difference, supporting))

    def retrieve_centers(self):
        centers = []
        for rig in self.rigs:
            segments = [('DEF-spine', .15), ('DEF-spine.002', .15), ('DEF-spine.003', .20),
                        ('DEF-spine.006', .08)]
            for side in ('L', 'R'):
                segments.extend([(f'DEF-thigh.{side}', .10), (f'DEF-shin.{side}', .05),
                                 (f'DEF-foot.{side}', .015), (f'DEF-upper_arm.{side}', .025),
                                 (f'DEF-forearm.{side}', .015), (f'DEF-hand.{side}', .005)])
            points = [(rig.matrix_world @ ((rig.pose.bones[name].head + rig.pose.bones[name].tail) * .5), weight)
                      for name, weight in segments if name in rig.pose.bones]
            centers.append(sum((np.array(point) * weight for point, weight in points), np.zeros(3)) /
                           sum(weight for _point, weight in points))
        return np.array(centers)

    def retrieve_residual(self, values, apply=True):
        if apply:
            self.variables.apply(values)
            self.update()
        positions = np.array([sample.retrieve_position() for sample in self.samples])
        residual = list(((positions - self.original) / math.sqrt(len(self.samples))).ravel() * 3)
        residual.extend(values * .08)
        residual.extend(np.minimum(positions[:, 2] - self.settings.floor, 0) * 8 /
                        math.sqrt(len(self.samples)))
        supports = []
        for participant, sample in self.floor_contacts:
            point = sample.retrieve_position()
            residual.append((point.z - self.settings.floor - .002) * 8)
            supports.append((participant, None, point))
        for source, target, sample, anchor, normal, original, supporting in self.pair_contacts:
            point, other = sample.retrieve_position(), anchor.retrieve_position()
            difference = point - other
            desired = original - normal * original.dot(normal) if supporting else original
            desired = anchor.retrieve_direction(desired)
            contact_error = difference - desired
            if not supporting:
                # Side contacts may slide vertically while retaining their surface separation.
                contact_error.z *= .1
            residual.extend(contact_error * 6)
            if supporting:
                supported, supporting_participant = (source, target) if supporting > 0 else (target, source)
                supports.append((supported, supporting_participant, (point + other) * .5))
        for sample, anchor, normal, original in self.collision_pairs:
            gap = (sample.retrieve_position() - anchor.retrieve_position()).dot(anchor.retrieve_direction(normal))
            residual.append(min(0, gap - original) * 10)
        residual.extend(self.self_collisions.retrieve_residual())
        centers = self.retrieve_centers()
        # A shared force solve transfers participant loads across their body contacts.
        masses = [float(rig.get('Ergonomic mass', 1.0)) for rig in self.rigs]
        masses = np.maximum(masses, .01)
        masses /= np.mean(masses)
        residual.extend(self.equilibrium.retrieve_residual(centers, masses, supports) * .7)
        return np.asarray(residual)

    def fit(self, values):
        residual = self.retrieve_residual(values)
        for iteration in range(self.settings.iterations):
            if iteration % 3 == 0:
                jacobian = np.empty((len(residual), len(values)))
                for column in range(len(values)):
                    sample = values.copy()
                    sample[column] += .0005
                    jacobian[:, column] = (self.retrieve_residual(sample) - residual) / .0005
            change = np.linalg.lstsq(np.vstack((jacobian, np.eye(len(values)) * .15)),
                                     np.concatenate((-residual, np.zeros(len(values)))), rcond=1e-6)[0]
            accepted = False
            for fraction in (1, .5, .25, .125):
                candidate = np.clip(values + change * fraction, -self.variables.bounds, self.variables.bounds)
                trial = self.retrieve_residual(candidate)
                if trial @ trial < residual @ residual - 1e-9:
                    displacement = candidate - values
                    denominator = displacement @ displacement
                    if denominator > 1e-12:
                        jacobian += np.outer(trial - residual - jacobian @ displacement,
                                             displacement) / denominator
                    values, residual = candidate, trial
                    accepted = True
                    break
            if not accepted or np.linalg.norm(change) < .0001:
                break
        self.variables.apply(values)
        self.update()
        return values

    def optimize(self, keyframe=False):
        values = np.zeros(len(self.variables.parameters))
        try:
            residual = self.retrieve_residual(values)
            initial = float(residual @ residual)
            for refinement in range(3):
                values = self.fit(values)
                surfaces = [BodySurface(self.context, rig) for rig in self.rigs]
                overlaps = self.self_collisions.retrieve_overlaps(surfaces)
                if overlaps:
                    if refinement == 2:
                        detail = overlaps[0]
                        raise ValueError(f"Arm clearance requires a larger movement range or an adjusted starting pose: "
                                         f"{detail['rig']} {detail['arm']} / {detail['body']}")
                    self.self_collisions.extend(surfaces)
                else:
                    break
            grounding = FloorPlacement(self).apply()
            surfaces = [BodySurface(self.context, rig) for rig in self.rigs]
            if self.self_collisions.retrieve_overlaps(surfaces):
                raise ValueError('Arm clearance requires a pose with compatible floor support')
            residual = self.retrieve_residual(values, apply=False)
            if keyframe:
                self.variables.keyframe()
            return {'initial': initial, 'final': float(residual @ residual),
                    'participants': len(self.rigs), 'floor_contacts': len(self.floor_contacts),
                    'body_contacts': len(self.pair_contacts), 'floor_adjustments': grounding}
        except Exception:
            self.variables.restore()
            self.update()
            raise


class ANIMATION_OT_make_ergonomic(bpy.types.Operator):
    bl_idname = 'animation.make_ergonomic'
    bl_label = 'Make ergonomic'
    bl_description = 'Adjust all animation participants together for nearby floor and body support, preserving the current pose'
    bl_options = {'REGISTER', 'UNDO'}

    floor: bpy.props.FloatProperty(name='Floor height', default=0, subtype='DISTANCE')
    proximity: bpy.props.FloatProperty(name='Contact distance', default=.06, min=.001, max=.3, subtype='DISTANCE')
    translation: bpy.props.FloatProperty(name='Maximum movement', default=.08, min=.001, max=.3, subtype='DISTANCE')
    rotation: bpy.props.FloatProperty(name='Maximum rotation', default=math.radians(10),
                                      min=0, max=math.radians(30), subtype='ANGLE')

    @classmethod
    def poll(cls, context):
        return context.mode in {'OBJECT', 'POSE'} and bool(ErgonomicPose.retrieve_participants(context))

    def execute(self, context):
        gravity = context.scene.gravity
        if abs(gravity.x) + abs(gravity.y) > .0001 or gravity.z >= 0:
            self.report({'ERROR'}, 'Use downward Z gravity for floor support')
            return {'CANCELLED'}
        try:
            rigs = ErgonomicPose.retrieve_participants(context)
            for rig in rigs:
                animation = rig.animation_data
                if animation and animation.action and not animation.action.is_editable:
                    raise ValueError(f'Choose an editable authoring action for {rig.name}')
                if animation and animation.use_nla and animation.action is None and animation.nla_tracks:
                    raise ValueError('Use Select animation to open its authoring strips before adjusting the pose')
            solver = ErgonomicPose(context, rigs, ErgonomicSettings(
                self.floor, self.proximity, self.translation, self.rotation))
            result = solver.optimize(context.scene.tool_settings.use_keyframe_insert_auto)
        except (ValueError, RuntimeError, np.linalg.LinAlgError) as error:
            self.report({'ERROR'}, str(error))
            return {'CANCELLED'}
        self.report({'INFO'}, f"Adjusted {result['participants']} participants together; "
                    f"{result['floor_contacts']} floor and {result['body_contacts']} body contacts")
        return {'FINISHED'}


def register():
    previous = bpy.types.Operator.bl_rna_get_subclass_py('ANIMATION_OT_make_ergonomic')
    if previous:
        bpy.utils.unregister_class(previous)
    bpy.utils.register_class(ANIMATION_OT_make_ergonomic)


def unregister():
    previous = bpy.types.Operator.bl_rna_get_subclass_py('ANIMATION_OT_make_ergonomic')
    if previous:
        bpy.utils.unregister_class(previous)
