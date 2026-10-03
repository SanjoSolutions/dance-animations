"""Native Blender constraints for receiver-relative prop and anatomy placement."""

import json

import bpy
from mathutils import Matrix, Vector

from contact_geometry import ContactMesh


FOOT_IK_CONTROLS = ('foot_ik.L', 'foot_ik.R')

PART_AUTO = 'AUTO'
PART_HAND_L = 'HAND_L'
PART_HAND_R = 'HAND_R'
HAND_PARTS = (PART_HAND_L, PART_HAND_R)

FINGER_KEYS = ('THUMB', 'INDEX', 'MIDDLE', 'RING', 'PINKY')
FINGER_DEF = {
    'THUMB': 'thumb',
    'INDEX': 'f_index',
    'MIDDLE': 'f_middle',
    'RING': 'f_ring',
    'PINKY': 'f_pinky',
}
DEFAULT_FINGERS = set(FINGER_KEYS)


class AnatomyBinding:
    """Resolved anatomy contact: tip bones, IK control, and shaft bones."""

    __slots__ = ('rig', 'part', 'control_bone', 'tip_bones', 'shaft_bones', 'shaft_radius', 'palm')

    def __init__(self, rig, part, control_bone, tip_bones, shaft_bones, shaft_radius, palm=None):
        self.rig = rig
        self.part = part
        self.control_bone = control_bone
        self.tip_bones = tuple(tip_bones)
        self.shaft_bones = tuple(shaft_bones)
        self.shaft_radius = shaft_radius
        self.palm = palm

    @property
    def is_hand(self):
        return self.part in HAND_PARTS

    @property
    def key(self):
        return (self.part, self.control_bone, self.tip_bones, self.shaft_bones)


class BoneDirectionOverlay:
    """Temporary rotation that preserves the control's authored channels."""

    def __init__(self, bone):
        self.name = bone.name
        self.mode = bone.rotation_mode
        self.property = {'QUATERNION': 'rotation_quaternion',
                         'AXIS_ANGLE': 'rotation_axis_angle'}.get(bone.rotation_mode, 'rotation_euler')
        self.baseline = tuple(getattr(bone, self.property))
        self.applied = self.baseline

    def matches(self, bone):
        return (bone.rotation_mode == self.mode and
                max(abs(first - second) for first, second in
                    zip(getattr(bone, self.property), self.applied)) < 1e-5)

    def restore(self, bone):
        if self.matches(bone):
            setattr(bone, self.property, self.baseline)

    def reapply(self, bone):
        setattr(bone, self.property, self.applied)

    def align(self, bone, destination):
        if not self.matches(bone):
            self.baseline = tuple(getattr(bone, self.property))
        location, scale = bone.location.copy(), bone.scale.copy()
        quaternion = bone.rotation_quaternion.copy()
        bone.matrix = destination
        bone.location, bone.scale = location, scale
        if bone.rotation_mode == 'QUATERNION':
            bone.rotation_quaternion.normalize()
            bone.rotation_quaternion.make_compatible(quaternion)
        self.applied = tuple(getattr(bone, self.property))


class PalmWristOverlay:
    """Let hand IK own the palm frame while retaining authored wrist tweak keys."""

    CONSTRAINT = 'Interactable palm wrist'

    def __init__(self, bone):
        self.bone = bone
        self.constraint = bone.constraints.new('LIMIT_ROTATION')
        self.constraint.name = self.CONSTRAINT
        self.constraint.owner_space = 'LOCAL'
        self.constraint.use_limit_x = True
        self.constraint.use_limit_y = True
        self.constraint.use_limit_z = True

    def release(self):
        self.bone.constraints.remove(self.constraint)

    @classmethod
    def clear_saved(cls):
        for rig in [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']:
            for name in ('hand_tweak.L', 'hand_tweak.R'):
                bone = rig.pose.bones.get(name)
                if bone:
                    constraint = bone.constraints.get(cls.CONSTRAINT)
                    if constraint:
                        bone.constraints.remove(constraint)


class FootPlacementOverlay:
    """Native world-space foot targets for a batched preview correction."""

    MARKER = 'interactable_foot_anchor'

    def __init__(self, rig, bone):
        self.bone = bone
        self.anchor = bpy.data.objects.new(f'{rig.name}.{bone.name}.interactable_foot', None)
        rig.users_collection[0].objects.link(self.anchor)
        self.anchor[self.MARKER] = True
        self.anchor.hide_render = True
        self.anchor.hide_select = True
        self.anchor.empty_display_size = 0.01
        self.constraint = bone.constraints.new('COPY_TRANSFORMS')
        self.constraint.name = 'Interactable foot placement'
        self.constraint.target = self.anchor
        self.constraint.owner_space = 'WORLD'
        self.constraint.target_space = 'WORLD'
        self.pause()

    def place(self, world):
        self.anchor.matrix_world = world
        self.constraint.mute = False

    def pause(self):
        self.constraint.mute = True

    def release(self):
        self.bone.constraints.remove(self.constraint)
        bpy.data.objects.remove(self.anchor, do_unlink=True)

    @classmethod
    def clear_saved(cls):
        anchors = {obj for obj in bpy.data.objects if obj.get(cls.MARKER)}
        if anchors:
            for rig in [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']:
                for bone in rig.pose.bones:
                    for constraint in list(bone.constraints):
                        if getattr(constraint, 'target', None) in anchors:
                            bone.constraints.remove(constraint)
            for anchor in anchors:
                bpy.data.objects.remove(anchor, do_unlink=True)


class InteractablePositioning:
    CONSTRAINT = 'Interactable positioning'
    DEPTH_EXPRESSION = 'min(depth, maximum) if maximum > 0 else depth'

    def __init__(self):
        # owner pointer -> (control bone name, baseline location, applied location)
        self.control_overrides = {}
        # owner pointer -> (arm parent bone, IK_FK, IK_Stretch) for hand binds
        self.ik_mode_overrides = {}
        # owner pointer -> {foot bone: (baseline matrix_basis, applied matrix_basis)}
        # Preserve planted Rigify feet while preview controls are active.
        self.foot_overrides = {}
        self.direction_overrides = {}
        self.palm_overrides = {}
        self.fast_foot_overrides = {}

    @property
    def hips_overrides(self):
        # Backward-compatible alias used by older call sites / tests.
        return self.control_overrides

    @hips_overrides.setter
    def hips_overrides(self, value):
        self.control_overrides = value

    @staticmethod
    def _hand_side(part):
        return 'L' if part == PART_HAND_L else 'R'

    @classmethod
    def _hand_bones_present(cls, rig, side):
        return (f'hand_ik.{side}' in rig.pose.bones
                and f'DEF-hand.{side}' in rig.pose.bones
                and f'DEF-f_index.03.{side}' in rig.pose.bones)

    @classmethod
    def supports_anatomy(cls, obj):
        if not (obj and obj.type == 'ARMATURE'):
            return False
        return cls._hand_bones_present(obj, 'L') or cls._hand_bones_present(obj, 'R')

    @staticmethod
    def is_anatomy(obj):
        """True when obj is a control rig currently usable as anatomy contact."""
        return InteractablePositioning.resolve_binding(obj, bpy.context.scene if bpy.context else None) is not None

    @classmethod
    def resolve_anatomy_rig(cls, obj, scene):
        if obj and obj.type == 'ARMATURE' and cls.supports_anatomy(obj):
            return obj
        if obj and obj.type == 'MESH' and obj.name.endswith('.body'):
            rig = scene.objects.get(obj.name[:-5] + '.rigify')
            if cls.supports_anatomy(rig):
                return rig
        if obj and obj.type == 'ARMATURE' and obj.name.endswith('.rigify_deform'):
            rig = scene.objects.get(obj.name.replace('.rigify_deform', '.rigify'))
            if cls.supports_anatomy(rig):
                return rig
        return None

    @classmethod
    def retrieve_selected_fingers(cls, rig):
        selected = set(getattr(rig, 'interactable_fingers', DEFAULT_FINGERS) or ())
        return [key for key in FINGER_KEYS if key in selected] or list(FINGER_KEYS)

    @classmethod
    def resolve_part(cls, rig):
        requested = getattr(rig, 'interactable_anatomy_part', PART_AUTO) or PART_AUTO
        if requested == PART_AUTO:
            return next((part for part in HAND_PARTS if cls._hand_bones_present(rig, cls._hand_side(part))), None)
        if requested in HAND_PARTS:
            side = cls._hand_side(requested)
            return requested if cls._hand_bones_present(rig, side) else None
        return None

    @classmethod
    def resolve_binding(cls, obj, scene=None, receiver=None):
        if obj is None:
            return None
        scene = scene or (bpy.context.scene if bpy.context else None)
        if obj.type == 'ARMATURE' and cls.supports_anatomy(obj):
            rig = obj
        elif scene is None:
            return None
        else:
            rig = cls.resolve_anatomy_rig(obj, scene)
            if not rig:
                return None
        part = cls.resolve_part(rig)
        if part is None:
            return None
        side = cls._hand_side(part)
        fingers = cls.retrieve_selected_fingers(rig)
        tip_bones = []
        shaft_bones = []
        for key in fingers:
            base = FINGER_DEF[key]
            for segment in ('01', '02', '03'):
                name = f'DEF-{base}.{segment}.{side}'
                if name in rig.pose.bones:
                    shaft_bones.append(name)
            tip = f'DEF-{base}.03.{side}'
            if tip in rig.pose.bones:
                tip_bones.append(tip)
        if not tip_bones:
            return None
        control_name = f'hand_ik.{side}'
        palm = None
        if receiver and receiver.interactable.hand_contact == 'PALM':
            calibration = rig.pose.bones[control_name].get('Snap Hand Calibration')
            if calibration:
                values = json.loads(calibration)['wrist']
                palm = Matrix([values[index:index + 4] for index in range(0, 16, 4)]).inverted()
        return AnatomyBinding(rig, part, control_name, tip_bones, shaft_bones, 0.01, palm)

    @staticmethod
    def retrieve_issue(receiver, obj, scene):
        targets = receiver.interactable.target_collection
        protected = set(targets.all_objects) if targets else {receiver.interactable.target_mesh}
        hierarchy = {obj, *obj.children_recursive}
        issue = ''
        binding = InteractablePositioning.resolve_binding(obj, scene, receiver)
        anatomy = binding.rig if binding else None
        if obj.name not in scene.objects or not obj.is_editable:
            issue = 'Choose an editable object in this scene.'
        elif binding:
            if binding.is_hand and receiver.interactable.hand_contact == 'PALM' and binding.palm is None:
                issue = 'Configure Snap Hand palm calibration on the contact rig.'
            elif anatomy in protected:
                issue = 'Choose anatomy separate from the receiver target meshes.'
            elif any(other != receiver and other.interactable.is_receiver
                     and other.interactable.auto_position and other.interactable.contact_object
                     and (InteractablePositioning.resolve_anatomy_rig(
                         other.interactable.contact_object, scene) == anatomy)
                     for other in scene.objects):
                issue = 'Assign each anatomy rig to one receiver.'
            elif Vector(anatomy.interactable_entry_direction).length_squared < 1e-12:
                issue = 'Set an entry direction with positive length.'
            elif (anatomy.interactable_direction_bone
                  and anatomy.interactable_direction_bone not in anatomy.pose.bones):
                issue = f'Direction bone "{anatomy.interactable_direction_bone}" is missing.'
            elif binding.control_bone not in anatomy.pose.bones:
                issue = f'Control bone "{binding.control_bone}" is missing.'
        elif InteractablePositioning.resolve_anatomy_rig(obj, scene) and not binding:
            issue = 'Choose an available hand on the contact rig.'
        elif receiver in hierarchy or hierarchy.intersection(protected) or obj.interactable.is_receiver:
            issue = 'Choose a prop hierarchy separate from the receiver and character.'
        elif any(other != receiver and other.interactable.is_receiver
                 and other.interactable.auto_position and other.interactable.contact_object
                 and ({other.interactable.contact_object, *other.interactable.contact_object.children_recursive}
                      .intersection(hierarchy)) for other in scene.objects):
            issue = 'Assign each prop hierarchy to one receiver.'
        elif Vector(obj.interactable_entry_direction).length_squared < 1e-12:
            issue = 'Set an entry direction with positive length.'
        return issue

    def release(self, settings):
        helper, owner = settings.position_helper, settings.position_owner
        if owner:
            self.release_fast_feet(owner)
        if owner and owner.as_pointer() in self.control_overrides:
            self._restore_control(owner)
        elif owner and helper:
            for constraint in list(owner.constraints):
                if constraint.type == 'COPY_TRANSFORMS' and constraint.target == helper:
                    owner.constraints.remove(constraint)
        settings.position_helper = None
        settings.position_owner = None
        if helper:
            bpy.data.objects.remove(helper, do_unlink=True)

    @staticmethod
    def _matrix_close(first, second, epsilon=1e-5):
        return max(abs(first[row][column] - second[row][column])
                   for row in range(4) for column in range(4)) < epsilon

    def _restore_control(self, owner):
        token = owner.as_pointer()
        previous = self.control_overrides.pop(token, None)
        ik_mode = self.ik_mode_overrides.pop(token, None)
        feet = self.foot_overrides.pop(token, None)
        direction = self.direction_overrides.pop(token, None)
        palm = self.palm_overrides.pop(token, None)
        if palm:
            palm.release()
        if direction and direction.name in owner.pose.bones:
            direction.restore(owner.pose.bones[direction.name])
        if ik_mode:
            parent_name, ik_fk, ik_stretch = ik_mode
            if parent_name in owner.pose.bones:
                parent = owner.pose.bones[parent_name]
                if ik_fk is not None and "IK_FK" in parent:
                    parent["IK_FK"] = ik_fk
                if ik_stretch is not None and "IK_Stretch" in parent:
                    parent["IK_Stretch"] = ik_stretch
        if previous:
            bone_name, baseline, applied = previous
            if bone_name in owner.pose.bones:
                bone = owner.pose.bones[bone_name]
                if (Vector(bone.location) - Vector(applied)).length < 1e-5:
                    bone.location = Vector(baseline)
        if feet:
            for name, (baseline, applied) in feet.items():
                if name not in owner.pose.bones:
                    continue
                bone = owner.pose.bones[name]
                if self._matrix_close(bone.matrix_basis, Matrix(applied)):
                    bone.matrix_basis = Matrix(baseline)

    def _restore_hips(self, owner):
        self._restore_control(owner)

    def restore_hips(self):
        self.restore_controls()

    def restore_controls(self):
        for overlay in self.fast_foot_overrides.values():
            overlay.pause()
        tokens = (set(self.control_overrides) | set(self.ik_mode_overrides)
                  | set(self.foot_overrides) | set(self.direction_overrides) | set(self.palm_overrides))
        for token in list(tokens):
            owner = next((obj for obj in bpy.data.objects if obj.as_pointer() == token), None)
            if owner:
                self._restore_control(owner)
            else:
                self.control_overrides.pop(token, None)
                self.ik_mode_overrides.pop(token, None)
                self.foot_overrides.pop(token, None)
                self.direction_overrides.pop(token, None)
                self.palm_overrides.pop(token, None)

    def release_fast_feet(self, rig=None):
        for key in list(self.fast_foot_overrides):
            if rig is None or key[0] == rig.as_pointer():
                self.fast_foot_overrides.pop(key).release()

    def clear_fast_feet(self):
        self.fast_foot_overrides.clear()
        FootPlacementOverlay.clear_saved()

    def _reapply_preview_controls(self, rig):
        changed = False
        token = rig.as_pointer()
        previous = self.control_overrides.get(token)
        if previous:
            name, baseline, applied = previous
            control = rig.pose.bones[name]
            if (control.location - Vector(applied)).length > 1e-5:
                control.location = applied
                changed = True
        direction = self.direction_overrides.get(token)
        if direction:
            bone = rig.pose.bones[direction.name]
            if bone.rotation_mode == direction.mode and not direction.matches(bone):
                direction.reapply(bone)
                changed = True
        if changed:
            rig.update_tag()
            bpy.context.view_layer.update()

    @staticmethod
    def retrieve_bone_tip_world(rig, bone_name, graph):
        evaluated = rig.evaluated_get(graph)
        bone = evaluated.pose.bones[bone_name]
        length = evaluated.data.bones[bone_name].length
        return evaluated.matrix_world @ bone.matrix @ Vector((0, length, 0))

    @classmethod
    def retrieve_tip_world(cls, binding, graph):
        if binding.palm is not None:
            return cls.retrieve_palm_world(binding, graph).translation
        else:
            tips = [cls.retrieve_bone_tip_world(binding.rig, name, graph) for name in binding.tip_bones]
            return sum(tips, Vector()) / len(tips)

    @classmethod
    def retrieve_palm_world(cls, binding, graph):
        evaluated = binding.rig.evaluated_get(graph)
        hand = evaluated.pose.bones[f'DEF-hand.{cls._hand_side(binding.part)}']
        return evaluated.matrix_world @ hand.matrix @ binding.palm

    @classmethod
    def retrieve_entry_direction(cls, binding, graph):
        if binding.palm is not None:
            return -cls.retrieve_palm_world(binding, graph).to_3x3().col[2].normalized()
        evaluated = binding.rig.evaluated_get(graph)
        world = evaluated.matrix_world
        custom = binding.rig.interactable_direction_bone
        hand_names = {binding.control_bone, f'DEF-hand.{cls._hand_side(binding.part)}'} if binding.is_hand else set()
        custom_bone = evaluated.pose.bones.get(custom)
        uses_custom = custom_bone and hand_names.intersection(
            bone.name for bone in [custom_bone, *custom_bone.parent_recursive])
        if uses_custom:
            direction = evaluated.pose.bones[custom].matrix.to_3x3() @ Vector(
                binding.rig.interactable_entry_direction)
            return (world.to_3x3() @ direction).normalized()
        axes = []
        for name in binding.tip_bones:
            bone = evaluated.pose.bones[name]
            axes.append(bone.matrix.to_3x3() @ Vector(binding.rig.interactable_entry_direction))
        direction = sum(axes, Vector())
        if direction.length_squared < 1e-12:
            # Fall back to hand → tip midpoint.
            side = cls._hand_side(binding.part) if binding.is_hand else None
            hand = evaluated.pose.bones.get(f'DEF-hand.{side}') if side else None
            tip = world.inverted() @ cls.retrieve_tip_world(binding, graph)
            if hand:
                origin = hand.matrix.translation
                direction = tip - origin
            else:
                direction = Vector(binding.rig.interactable_entry_direction)
        return (world.to_3x3() @ direction).normalized()

    @staticmethod
    def retrieve_calibration(obj, graph, scene=None, receiver=None):
        scene = scene or bpy.context.scene
        binding = InteractablePositioning.resolve_binding(obj, scene, receiver)
        if binding:
            return InteractablePositioning._calibrate_anatomy(binding, graph)
        evaluated = obj.evaluated_get(graph)
        world = evaluated.matrix_world.copy()
        if abs(world.determinant()) < 1e-12:
            raise ValueError('Use an object with positive scale on every axis.')
        direction = Vector(obj.interactable_entry_direction)
        if obj.type == 'ARMATURE' and obj.interactable_direction_bone in evaluated.pose.bones:
            direction = evaluated.pose.bones[obj.interactable_direction_bone].matrix.to_3x3() @ direction
        direction.normalize()
        inverse = world.inverted()
        vertices = [inverse @ Vector(point) for mesh in [obj, *obj.children_recursive] if mesh.type == 'MESH'
                    for point in ContactMesh.from_object(mesh, graph).vertices]
        if vertices:
            maximum = max(point.dot(direction) for point in vertices)
            tip_vertices = [point for point in vertices if maximum - point.dot(direction) < 1e-5]
            tip = sum(tip_vertices, Vector()) / len(tip_vertices)
        else:
            tip = Vector()
        return tip, direction, world.to_scale()

    @staticmethod
    def _calibrate_anatomy(binding, graph):
        rig = binding.rig
        evaluated = rig.evaluated_get(graph)
        world = evaluated.matrix_world.copy()
        if abs(world.determinant()) < 1e-12:
            raise ValueError('Use an anatomy rig with positive scale on every axis.')
        tip_world = InteractablePositioning.retrieve_tip_world(binding, graph)
        direction = InteractablePositioning.retrieve_entry_direction(binding, graph)
        tip = world.inverted() @ tip_world
        return tip, (world.inverted().to_3x3() @ direction).normalized(), world.to_scale()

    def bind(self, receiver, obj, graph, approximate=False):
        scene = receiver.users_scene[0] if receiver.users_scene else bpy.context.scene
        binding = self.resolve_binding(obj, scene, receiver)
        if binding:
            self._bind_anatomy(receiver, binding, graph, approximate=approximate)
        else:
            self._bind_prop(receiver, obj, graph)

    def _create_helper(self, receiver):
        helper = bpy.data.objects.new(receiver.name + '.position', None)
        receiver.users_collection[0].objects.link(helper)
        helper.parent = receiver
        helper.hide_render = True
        helper.hide_select = True
        helper.empty_display_size = 0.01
        return helper

    @staticmethod
    def retrieve_depth(settings):
        maximum = settings.position_depth_maximum
        return min(settings.position_depth, maximum) if maximum > 0 else settings.position_depth

    @staticmethod
    def _configure_depth_driver(helper, receiver):
        curve = helper.driver_add('location', 1)
        for name, path in (('depth', 'position_depth'), ('maximum', 'position_depth_maximum')):
            variable = curve.driver.variables.new()
            variable.name = name
            variable.targets[0].id = receiver
            variable.targets[0].data_path = 'interactable.' + path
        curve.driver.expression = InteractablePositioning.DEPTH_EXPRESSION

    def _bind_prop(self, receiver, obj, graph):
        settings = receiver.interactable
        tip, direction, scale = self.retrieve_calibration(obj, graph)
        helper = self._create_helper(receiver)
        settings.position_helper = helper
        settings.position_owner = obj
        settings.position_tip = tip
        settings.position_direction = direction
        settings.position_scale = scale
        constraint = obj.constraints.new('COPY_TRANSFORMS')
        constraint.name = self.CONSTRAINT
        constraint.target = helper
        constraint.owner_space = 'WORLD'
        constraint.target_space = 'WORLD'
        self._configure_depth_driver(helper, receiver)
        self.update_transform(settings)

    def _bind_anatomy(self, receiver, binding, graph, approximate=False):
        settings = receiver.interactable
        tip, direction, scale = self._calibrate_anatomy(binding, graph)
        helper = self._create_helper(receiver)
        helper['interactable_anatomy'] = True
        helper['interactable_hand_contact'] = settings.hand_contact
        settings.position_helper = helper
        settings.position_owner = binding.rig
        settings.position_tip = tip
        settings.position_direction = direction
        settings.position_scale = scale
        control = binding.rig.pose.bones[binding.control_bone]
        token = binding.rig.as_pointer()
        self.control_overrides[token] = (
            binding.control_bone, tuple(control.location), tuple(control.location))
        self._configure_depth_driver(helper, receiver)
        helper.rotation_mode = 'QUATERNION'
        helper.rotation_quaternion = (1, 0, 0, 0)
        helper.scale = (1, 1, 1)
        helper.location = (0.0, self.retrieve_depth(settings), 0.0)
        self.update_anatomy(settings, graph, approximate=approximate)

    def _prepare_hand_ik(self, binding):
        if binding.is_hand:
            rig = binding.rig
            if binding.palm is not None:
                tweak = rig.pose.bones.get(f'hand_tweak.{self._hand_side(binding.part)}')
                if tweak:
                    token = rig.as_pointer()
                    overlay = self.palm_overrides.get(token)
                    if overlay is None:
                        overlay = PalmWristOverlay(tweak)
                        self.palm_overrides[token] = overlay
                        rig.update_tag()
                        bpy.context.view_layer.update()
            parent_name = f'upper_arm_parent.{self._hand_side(binding.part)}'
            parent = rig.pose.bones.get(parent_name)
            if parent:
                token = rig.as_pointer()
                if token not in self.ik_mode_overrides:
                    self.ik_mode_overrides[token] = (
                        parent_name, parent.get('IK_FK'), parent.get('IK_Stretch'))
                changed = False
                for property in ('IK_FK', 'IK_Stretch'):
                    if property in parent and parent[property] != 0.0:
                        parent[property] = 0.0
                        changed = True
                if changed:
                    rig.update_tag()
                    bpy.context.view_layer.update()

    @staticmethod
    def update_transform(settings):
        owner = settings.position_owner
        if owner and settings.position_helper and settings.position_helper.get('interactable_anatomy'):
            helper = settings.position_helper
            if helper:
                helper.location = (0.0, POSITIONING.retrieve_depth(settings), 0.0)
                if helper.animation_data and helper.animation_data.drivers:
                    helper.animation_data.drivers[0].driver.expression = POSITIONING.DEPTH_EXPRESSION
            return
        helper = settings.position_helper
        direction = Vector(settings.position_direction)
        scale = Vector(settings.position_scale)
        scaled_direction = Vector([direction[i] * scale[i] for i in range(3)])
        rotation = scaled_direction.rotation_difference(Vector((0, 1, 0)))
        basis = rotation.to_matrix() @ Matrix.Diagonal(scale)
        location = -(basis @ Vector(settings.position_tip))
        helper.rotation_mode = 'QUATERNION'
        helper.rotation_quaternion = rotation
        helper.scale = scale
        helper.location = location
        helper.location.y += POSITIONING.retrieve_depth(settings)
        helper.animation_data.drivers[0].driver.expression = (
            f'{location.y!r} + ({POSITIONING.DEPTH_EXPRESSION})')

    def _capture_foot_ik_world(self, rig):
        worlds = {}
        for name in FOOT_IK_CONTROLS:
            if name not in rig.pose.bones:
                continue
            bone = rig.pose.bones[name]
            worlds[name] = (rig.matrix_world @ bone.matrix).copy()
        return worlds

    def _replant_foot_ik(self, rig, token, worlds):
        # Keep foot IK targets planted while positioning controls.
        if not worlds:
            self.foot_overrides.pop(token, None)
            return
        previous = self.foot_overrides.get(token, {})
        stored = {}
        for name, world in worlds.items():
            bone = rig.pose.bones[name]
            baseline = bone.matrix_basis.copy()
            prior = previous.get(name)
            if prior and self._matrix_close(baseline, Matrix(prior[1])):
                baseline = Matrix(prior[0])
            bone.matrix = rig.matrix_world.inverted() @ world
            stored[name] = (tuple(tuple(row) for row in baseline),
                            tuple(tuple(row) for row in bone.matrix_basis))
        self.foot_overrides[token] = stored

    def _align_anatomy_direction(self, binding, receiving, graph, evaluate=True):
        rig = binding.rig
        tip = self.retrieve_tip_world(binding, graph)
        expected = (receiving.to_3x3() @ Vector((0, 1, 0))).normalized()
        direction = self.retrieve_entry_direction(binding, graph)
        if binding.palm is not None:
            palm = self.retrieve_palm_world(binding, graph)
            desired = receiving.to_3x3() @ Matrix(((1, 0, 0), (0, 0, -1), (0, 1, 0)))
            correction = (desired @ palm.to_3x3().inverted()).to_4x4()
            needs_alignment = correction.to_quaternion().angle > 1e-5
        else:
            correction = direction.rotation_difference(expected).to_matrix().to_4x4()
            needs_alignment = (direction - expected).length > 1e-5
        if needs_alignment:
            name = binding.control_bone
            bone = rig.pose.bones[name]
            token = rig.as_pointer()
            overlay = self.direction_overrides.get(token)
            if overlay and overlay.name != name:
                overlay.restore(rig.pose.bones[overlay.name])
                overlay = None
            if overlay and overlay.mode != bone.rotation_mode:
                overlay = None
            if overlay is None:
                overlay = BoneDirectionOverlay(bone)
                self.direction_overrides[token] = overlay
            world = rig.evaluated_get(graph).matrix_world @ rig.evaluated_get(graph).pose.bones[name].matrix
            destination = correction @ world
            destination.translation = world.translation
            tip = world.translation + correction.to_3x3() @ (tip - world.translation)
            overlay.align(bone, rig.matrix_world.inverted() @ destination)
            rig.update_tag()
            if evaluate:
                bpy.context.view_layer.update()
        return tip

    def update_anatomy(self, settings, graph=None, approximate=False):
        rig = settings.position_owner
        helper = settings.position_helper
        if not (rig and helper):
            return
        scene = rig.users_scene[0] if rig.users_scene else bpy.context.scene
        binding = self.resolve_binding(rig, scene, settings.id_data)
        if not binding:
            return
        self._prepare_hand_ik(binding)
        graph = graph or bpy.context.evaluated_depsgraph_get()
        for iteration in range(1 if approximate else 8):
            receiving = (helper.parent.evaluated_get(graph).matrix_world.copy()
                         if helper.parent else helper.matrix_world.copy())
            target = (receiving @ Vector((0.0, self.retrieve_depth(settings), 0.0))
                      if helper.parent else receiving.translation)
            aligned_tip = self._align_anatomy_direction(binding, receiving, graph, evaluate=not approximate)
            if not approximate:
                graph = bpy.context.evaluated_depsgraph_get()
            self._position_anatomy_tip(binding, target, graph, tip=aligned_tip if approximate else None,
                                      approximate=approximate)
            rig.update_tag()
            bpy.context.view_layer.update()
            if approximate:
                self._reapply_preview_controls(rig)
            graph = bpy.context.evaluated_depsgraph_get()
            direction = self.retrieve_entry_direction(binding, graph)
            expected = (receiving.to_3x3() @ Vector((0, 1, 0))).normalized()
            tip = self.retrieve_tip_world(binding, graph)
            if (tip - target).length < 1e-5 and (direction - expected).length < 1e-5:
                break

    def _position_anatomy_tip(self, binding, target, graph, tip=None, approximate=False):
        rig = binding.rig
        tip = self.retrieve_tip_world(binding, graph) if tip is None else tip
        delta = target - tip
        if delta.length < 1e-7:
            return
        control = rig.pose.bones[binding.control_bone]
        token = rig.as_pointer()
        current = Vector(control.location)
        previous = self.control_overrides.get(token)
        if previous and previous[0] == binding.control_bone and (current - Vector(previous[2])).length < 1e-5:
            baseline = Vector(previous[1])
        else:
            baseline = current
        parent = control.parent
        parent_transforms = ({'parent_matrix': parent.matrix,
                              'parent_matrix_local': parent.bone.matrix_local} if parent else {})
        destination = control.matrix.copy()
        source = control.bone.convert_local_to_pose(
            destination, control.bone.matrix_local, invert=True, **parent_transforms)
        destination.translation += rig.matrix_world.to_3x3().inverted() @ delta
        translated = control.bone.convert_local_to_pose(
            destination, control.bone.matrix_local, invert=True, **parent_transforms)
        applied = current + translated.translation - source.translation
        control.location = applied
        self.control_overrides[token] = (binding.control_bone, tuple(baseline), tuple(applied))
    def synchronize(self, scene, graph, approximate=False):
        if not approximate:
            self.release_fast_feet()
        changed = False
        for receiver in [obj for obj in scene.objects if obj.interactable.is_receiver]:
            settings = receiver.interactable
            if settings.is_receiver:
                obj = settings.contact_object
                active = settings.auto_position and settings.enabled and obj is not None
                issue = self.retrieve_issue(receiver, obj, scene) if active else ''
                if settings.position_message != issue:
                    settings.position_message = issue
                usable = active and not issue
                binding = self.resolve_binding(obj, scene, receiver) if obj else None
                expected_owner = binding.rig if binding else obj
                previous = self.control_overrides.get(
                    settings.position_owner.as_pointer()) if settings.position_owner else None
                binding_changed = bool(
                    binding and previous and previous[0] != binding.control_bone)
                was_anatomy = bool(settings.position_helper and settings.position_helper.get('interactable_anatomy'))
                contact_changed = bool(was_anatomy and
                                       settings.position_helper.get('interactable_hand_contact', 'FINGERTIPS')
                                       != settings.hand_contact)
                if settings.position_helper and (not usable or settings.position_owner != expected_owner
                                                 or bool(binding) != was_anatomy
                                                 or binding_changed or contact_changed):
                    self.release(settings)
                    changed = True
                if usable and settings.position_helper is None:
                    try:
                        self.bind(receiver, obj, graph, approximate=approximate)
                        changed = True
                    except ValueError as error:
                        settings.position_message = str(error)
                elif usable and binding:
                    self.update_anatomy(settings, graph, approximate=approximate)
        return changed


POSITIONING = InteractablePositioning()
