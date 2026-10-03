"""Conservative current-frame Rigify repair through editable authoring controls."""

from dataclasses import dataclass
import math

import bpy
import numpy as np
from mathutils import Euler, Quaternion, Vector

from ergonomic_pose import ErgonomicPose
from natural_pose_limits import PoseAnatomy
from natural_pose_collisions import AnatomicalSurface, BodyClearance
from natural_pose_samples import PoseSurfaceSamples
from natural_pose_step import PoseStep


@dataclass
class NaturalPoseSettings:
    """Movement uses world units; rotation uses radians."""

    translation: float = .3
    rotation: float = math.pi / 2
    iterations: int = 18


class PoseControls:
    """Capture channels exactly and vary the available Rigify degrees of freedom."""

    def __init__(self, rigs, settings, finger_controls, finger_attachments=()):
        self.controls = []
        self.parameters = []
        self.bounds = []
        for rig in rigs:
            specifications = {name: (True, True, True) for name in
                              ('root', 'torso', 'hips', 'chest', 'neck', 'head')}
            for side in ('L', 'R'):
                specifications[f'shoulder.{side}'] = (False, True, True)
                for limb, parent in (('hand', 'upper_arm'), ('foot', 'thigh')):
                    settings_bone = rig.pose.bones.get(f'{parent}_parent.{side}')
                    if settings_bone:
                        blend = settings_bone.get('IK_FK', 0)
                        if blend < 1:
                            specifications[f'{limb}_ik.{side}'] = (True, True, True)
                            pole = settings_bone.get('pole_vector', False)
                            specifications[f'{parent}_ik_target.{side}' if pole else f'{parent}_ik.{side}'] = (
                                bool(pole), not pole, False)
                            if limb == 'foot':
                                specifications[f'foot_heel_ik.{side}'] = (False, True, False)
                        if blend > 0:
                            chain = ('upper_arm', 'forearm', 'hand') if limb == 'hand' else ('thigh', 'shin', 'foot')
                            specifications.update({f'{part}_fk.{side}': (True, True, True) for part in chain})
                for name in finger_controls.get(rig.name, []):
                    specifications[name] = ((rig.name, name) in finger_attachments, True, True)
            for name, enabled in specifications.items():
                bone = rig.pose.bones.get(name)
                if bone:
                    path = ('rotation_quaternion' if bone.rotation_mode == 'QUATERNION' else
                            'rotation_axis_angle' if bone.rotation_mode == 'AXIS_ANGLE' else 'rotation_euler')
                    original = {field: tuple(getattr(bone, field)) for field in ('location', path, 'scale')}
                    index = len(self.controls)
                    self.controls.append((bone, path, original))
                    scale = (rig.matrix_world @ bone.matrix).to_scale()
                    drivers = {curve.data_path for curve in rig.animation_data.drivers} if rig.animation_data else set()
                    for mode, allowed, locks, bound in (
                            ('location', enabled[0] and not bone.bone.use_connect, bone.lock_location, settings.translation),
                            ('rotation', enabled[1], bone.lock_rotation, settings.rotation),
                            ('scale', enabled[2], bone.lock_scale, .5)):
                        property_path = path if mode == 'rotation' else mode
                        # Quaternion component locks require a dedicated constrained parameterization.
                        locked_rotation = mode == 'rotation' and path != 'rotation_euler' and (
                            any(bone.lock_rotation) or (bone.lock_rotations_4d and bone.lock_rotation_w))
                        if allowed and not locked_rotation and bone.path_from_id(property_path) not in drivers:
                            for axis in range(3):
                                if not locks[axis] and (mode != 'scale' or abs(original['scale'][axis] - 1) > .0001):
                                    self.parameters.append((index, mode, axis))
                                    self.bounds.append(bound / max(abs(scale[axis]), 1e-6) if mode == 'location' else bound)
        self.bounds = np.array(self.bounds)
        self.applied = np.zeros(len(self.parameters))

    def apply(self, values):
        changed = {index for value, previous, (index, _mode, _axis)
                   in zip(values, self.applied, self.parameters) if value != previous}
        channels = {index: {field: list(value) for field, value in self.controls[index][2].items()}
                    for index in changed}
        rotations = {index: [0, 0, 0] for index in changed}
        for value, (index, mode, axis) in zip(values, self.parameters):
            if index in changed:
                _bone, path, original = self.controls[index]
                if mode == 'rotation':
                    if path == 'rotation_euler':
                        channels[index][path][axis] = original[path][axis] + value
                    else:
                        rotations[index][axis] = value
                else:
                    channels[index][mode][axis] = original[mode][axis] + value
        for index in changed:
            bone, path, original = self.controls[index]
            if path != 'rotation_euler':
                initial = (Quaternion(original[path]) if path == 'rotation_quaternion' else
                           Quaternion(Vector(original[path][1:]), original[path][0]))
                rotation = initial @ Euler(rotations[index], 'XYZ').to_quaternion()
                if path == 'rotation_quaternion':
                    channels[index][path] = tuple(rotation)
                else:
                    axis, angle = rotation.to_axis_angle()
                    channels[index][path] = (angle, *axis)
            for field, value in channels[index].items():
                if tuple(getattr(bone, field)) != tuple(value):
                    setattr(bone, field, value)
        self.applied = values.copy()

    def restore(self):
        for bone, _path, original in self.controls:
            for field, value in original.items():
                setattr(bone, field, value)
        self.applied = np.zeros(len(self.parameters))

    def retrieve_changes(self):
        return [(bone, field) for bone, _path, original in self.controls for field, previous in original.items()
                if max(abs(first - second) for first, second in zip(getattr(bone, field), previous)) > 1e-5]

    def keyframe(self):
        changes = self.retrieve_changes()
        for bone, field in changes:
            animation = bone.id_data.animation_data
            if animation and animation.action:
                path = bone.path_from_id(field)
                curves = [curve for layer in animation.action.layers for strip in layer.strips
                          for bag in strip.channelbags if bag.slot_handle == animation.action_slot_handle
                          for curve in bag.fcurves if curve.data_path == path]
                if any(curve.lock or (curve.group and curve.group.lock) for curve in curves):
                    raise ValueError(f'Allow keyframe editing for {bone.id_data.name}: {bone.name}')
        for bone, field in changes:
            if not bone.keyframe_insert(field, group=bone.name):
                raise ValueError(f'Choose editable animation channels for {bone.id_data.name}: {bone.name}')


class NaturalPose:
    def __init__(self, context, rigs, settings=None):
        self.context = context
        self.rigs = list(rigs)
        self.settings = settings or NaturalPoseSettings()
        if not self.rigs:
            raise ValueError('Choose character participants or select a Rigify character')
        for rig in self.rigs:
            if not rig.is_editable:
                raise ValueError(f'Choose an editable authoring rig for {rig.name}')
            animation = rig.animation_data
            if animation and animation.action and not animation.action.is_editable:
                raise ValueError(f'Choose an editable authoring action for {rig.name}')
            if animation and animation.use_nla and animation.action is None and animation.nla_tracks:
                raise ValueError('Use Select animation to open its authoring strips before fixing the pose')
        self.update()
        self.anatomy = PoseAnatomy(self.rigs)
        if not self.anatomy.joints:
            raise ValueError('Choose a Rigify character with anatomical ORG bones')
        self.surfaces = self.retrieve_surfaces()
        self.collisions = BodyClearance(self.surfaces, max(.05, self.settings.translation * 2))
        fingers = {}
        finger_attachments = set()
        for joint in self.anatomy.joints:
            if joint.child.name.startswith(('f_', 'thumb')) and max(abs(joint.retrieve_error())) > .001:
                fingers.setdefault(joint.rig.name, []).append(joint.child.name)
        for span in self.anatomy.spans:
            if span.bone.name.startswith(('f_', 'thumb', 'hand_tweak')) and max(abs(span.retrieve_error())) > .001:
                fingers.setdefault(span.rig.name, []).append(span.bone.name)
                finger_attachments.add((span.rig.name, span.bone.name))
        self.anatomical_fingers = {(rig, name) for rig, names in fingers.items() for name in names}
        for first, second in self.collisions.retrieve_pairs(self.surfaces):
            for patch in (first, second):
                if patch.region.startswith(('f_', 'thumb')):
                    names = fingers.setdefault(patch.surface.rig.name, [])
                    finger, _segment, side = patch.region.split('.')[:3]
                    names.extend(f'{finger}.{segment:02}.{side}' for segment in (1, 2, 3))
                    names.append(f'{finger}.01_master.{side}')
        self.variables = PoseControls(self.rigs, self.settings, fingers, finger_attachments)
        self.samples = [sample for surface in self.surfaces for samples in surface.regions.values() for sample in samples]
        self.original = np.array([sample.retrieve_position() for sample in self.samples])
        self.surface_samples = PoseSurfaceSamples(self.samples, self.collisions.separations)

    @staticmethod
    def retrieve_participants(context):
        participants = ErgonomicPose.retrieve_participants(context)
        if participants:
            return participants
        else:
            return [obj for obj in context.selected_objects if obj.type == 'ARMATURE'
                    and 'ORG-spine' in obj.pose.bones and obj.is_editable]

    def update(self):
        self.context.view_layer.update()

    def retrieve_surfaces(self):
        return [AnatomicalSurface(self.context, rig) for rig in self.rigs]

    def retrieve_issues(self, surfaces):
        issues = self.anatomy.retrieve_issues()
        issues.extend(f"{overlap['rig']}: {overlap['arm']} / {overlap['body_rig']}: {overlap['body']} skin overlap"
                      for overlap in self.collisions.retrieve_overlaps(surfaces))
        return issues

    def retrieve_residual(self, values, strength):
        self.variables.apply(values)
        self.update()
        positions, collisions = self.surface_samples.retrieve()
        movement = ((positions - self.original) / math.sqrt(max(1, len(self.samples)))).ravel()
        constraints = np.concatenate((self.anatomy.retrieve_residual(), collisions))
        return np.concatenate((movement, values * .005, constraints * strength))

    def fit(self, values, strength, parameters=None, complete=None, iterations=None, preserve_anatomy=False):
        parameters = np.arange(len(values)) if parameters is None else np.array(parameters, dtype=int)
        residual = self.retrieve_residual(values, strength)
        refresh = True
        damping = .1
        for iteration in range(self.settings.iterations if iterations is None else min(iterations, self.settings.iterations)):
            refreshed = refresh
            if refresh:
                jacobian = np.empty((len(residual), len(parameters)))
                for column, parameter in enumerate(parameters):
                    sample = values.copy()
                    sample[parameter] += .001
                    forward = self.retrieve_residual(sample, strength)
                    sample[parameter] -= .002
                    backward = self.retrieve_residual(sample, strength)
                    jacobian[:, column] = (forward - backward) / .002
                refresh = False
            change = PoseStep(jacobian / strength, residual / strength,
                              self.variables.bounds[parameters], values[parameters], damping=damping).retrieve()
            accepted = False
            for fraction in (1, .5, .25, .125, .0625, .03125, .015625):
                candidate = values.copy()
                candidate[parameters] = np.clip(values[parameters] + fraction * change,
                                                -self.variables.bounds[parameters], self.variables.bounds[parameters])
                trial = self.retrieve_residual(candidate, strength)
                if (trial @ trial < residual @ residual - 1e-12
                        and (not preserve_anatomy or not self.anatomy.retrieve_issues())):
                    step = (candidate - values)[parameters]
                    if step @ step > 1e-14:
                        jacobian += np.outer(trial - residual - jacobian @ step, step) / (step @ step)
                    values, residual = candidate, trial
                    accepted = True
                    damping = max(.0009, damping * (.5 if fraction >= .5 else 2))
                    refresh = (iteration + 1) % 6 == 0
                    break
            if (accepted and complete and complete()) or np.linalg.norm(change) < 1e-6:
                break
            elif not accepted:
                damping *= 10
                refresh = not refreshed
        self.variables.apply(values)
        self.update()
        return values

    def repair_anatomy(self, values):
        parameters = [index for index, (control, _mode, _axis) in enumerate(self.variables.parameters)
                      if not self.variables.controls[control][0].name.startswith(('f_', 'thumb'))
                      or (self.variables.controls[control][0].id_data.name,
                          self.variables.controls[control][0].name) in self.anatomical_fingers]
        self.surface_samples = PoseSurfaceSamples(self.samples, [])
        for _attempt in range(3):
            values = self.fit(values, 100, parameters, complete=lambda: not self.anatomy.retrieve_issues())
            if not self.anatomy.retrieve_issues():
                break
        return values

    def refresh_contacts(self):
        surfaces = self.retrieve_surfaces()
        self.collisions = BodyClearance(surfaces, self.collisions.reach)
        self.surface_samples = PoseSurfaceSamples(self.samples, self.collisions.separations)
        return surfaces

    def fix(self, keyframe=False):
        initial = self.retrieve_issues(self.surfaces)
        changes = []
        remaining = []
        try:
            if initial:
                values = np.zeros(len(self.variables.parameters))
                if self.anatomy.retrieve_issues():
                    values = self.repair_anatomy(values)
                issues = self.anatomy.retrieve_issues()
                if issues:
                    raise ValueError('Starting pose restored. Adjust controls or increase correction bounds: '
                                     + '; '.join(issues[:3]))
                surfaces = self.refresh_contacts()
                remaining = self.retrieve_issues(surfaces)
                # Body translations provide a compact first pass for contacts;
                # the verified anatomical pose remains the recovery point.
                parameters = [index for index, (control, mode, _axis) in enumerate(self.variables.parameters)
                              if mode == 'location' and not
                              self.variables.controls[control][0].name.startswith(('f_', 'thumb'))]
                best = values.copy()
                for strength in (1, 10, 100):
                    if remaining and len(parameters):
                        values = self.fit(values, strength, parameters, iterations=6, preserve_anatomy=True)
                        surfaces = self.refresh_contacts()
                        issues = self.retrieve_issues(surfaces)
                        if not self.anatomy.retrieve_issues() and len(issues) < len(remaining):
                            best, remaining = values.copy(), issues
                        else:
                            values = best.copy()
                            self.variables.apply(values)
                            self.update()
                            self.refresh_contacts()
                            break
                    else:
                        break
                self.variables.apply(best)
                self.update()
                issues = self.anatomy.retrieve_issues()
                if issues:
                    raise ValueError('Starting pose restored. Anatomical checks require further correction: '
                                     + '; '.join(issues[:3]))
                remaining = self.retrieve_issues(self.retrieve_surfaces())
                changes = self.variables.retrieve_changes()
                if keyframe:
                    self.variables.keyframe()
            return {'corrected': max(0, len(initial) - len(remaining)), 'changed': len(changes),
                    'participants': len(self.rigs), 'remaining': remaining}
        except Exception:
            self.variables.restore()
            self.update()
            raise


class POSING_OT_fix_unnatural_pose(bpy.types.Operator):
    bl_idname = 'posing.fix_unnatural_pose'
    bl_label = 'Fix unnatural pose'
    bl_description = ('Repair joint ranges, skeletal distances, and body intersections at the current frame '
                      'with small pose changes; uses approximate Rigify anatomy')
    bl_options = {'REGISTER', 'UNDO'}

    translation: bpy.props.FloatProperty(name='Maximum movement', default=.3, min=.001, max=2, subtype='DISTANCE')
    rotation: bpy.props.FloatProperty(name='Maximum rotation', default=math.pi / 2,
                                      min=.01, max=math.pi, subtype='ANGLE')

    @classmethod
    def poll(cls, context):
        return context.mode in {'OBJECT', 'POSE'} and bool(NaturalPose.retrieve_participants(context))

    def execute(self, context):
        try:
            solver = NaturalPose(context, NaturalPose.retrieve_participants(context),
                                 NaturalPoseSettings(self.translation, self.rotation))
            result = solver.fix(context.scene.tool_settings.use_keyframe_insert_auto)
        except (ValueError, RuntimeError, np.linalg.LinAlgError) as error:
            self.report({'ERROR'}, str(error))
            return {'CANCELLED'}
        if result['remaining']:
            self.report({'WARNING'}, 'Joint and skeletal checks pass. '
                        f"{len(result['remaining'])} contacts need review: " + '; '.join(result['remaining']))
        else:
            message = (f"Corrected {result['corrected']} pose checks across {result['participants']} characters"
                       if result['changed'] else 'Current pose passes the modeled joint and body-clearance checks')
            self.report({'INFO'}, message)
        return {'FINISHED'}
