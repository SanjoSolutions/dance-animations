"""Automatic contact response during Blender posing and animation evaluation."""

from contextlib import contextmanager

import bpy
from bpy.app.handlers import persistent
from mathutils import Vector

from contact_geometry import ContactMeasurement, ContactMesh, EntryIntersection, ReceivingCylinder
from interactable_positioning import POSITIONING, PalmWristOverlay

DEPTH_PATH = "interactable.position_depth"
_depth_key_suppress = 0


@contextmanager
def suppress_depth_keying():
    """Skip Depth auto-key while bulk-assigning keyed curves or test fixtures."""
    global _depth_key_suppress
    _depth_key_suppress += 1
    try:
        yield
    finally:
        _depth_key_suppress -= 1


class ShapeKeyResponse:
    """Overlay contact values and retain authored values for release and saving."""

    def __init__(self):
        self.values = {}

    def apply(self, targets):
        for token in set(self.values) - set(targets):
            self._restore(token)
        for key, value in targets.items():
            value = max(key.slider_min, min(key.slider_max, value))
            previous = self.values.get(key)
            baseline = previous[0] if previous and abs(key.value-previous[1]) < 1e-6 else key.value
            if abs(key.value-value) > 1e-6:
                key.value = value
            self.values[key] = (baseline, value)

    def _restore(self, key):
        baseline, applied = self.values.pop(key)
        try:
            if abs(key.value-applied) < 1e-6:
                key.value = baseline
        except ReferenceError:
            pass

    def restore(self):
        for key in list(self.values):
            self._restore(key)


class InteractableSystem:
    def __init__(self):
        self.response = ShapeKeyResponse()
        self.measurement = EntryIntersection()
        self.busy = False
        self.suspended = False
        self.status = {}
        self.contacts = {}
        self.full_evaluation_depth = 0

    def uses_fast_mode(self, scene, graph):
        return (getattr(scene, 'interactable_fast_mode', False) and
                graph.mode == 'VIEWPORT' and self.full_evaluation_depth == 0)

    @contextmanager
    def full_evaluation(self):
        """Evaluate contact and placement while retaining the preview preference."""
        self.full_evaluation_depth += 1
        try:
            yield
        finally:
            self.full_evaluation_depth -= 1
            scene = bpy.context.scene
            if self.full_evaluation_depth == 0 and getattr(scene, 'interactable_fast_mode', False):
                self.refresh(scene, bpy.context.evaluated_depsgraph_get())

    def _refresh_fast_preview(self, scene, graph):
        self.response.restore()
        POSITIONING.synchronize(scene, graph, approximate=True)
        self.status.clear()
        self.contacts.clear()

    @staticmethod
    def retrieve_receivers(scene):
        return [obj for obj in scene.objects if obj.interactable.is_receiver]

    @staticmethod
    def retrieve_targets(settings):
        objects = settings.target_collection.all_objects if settings.target_collection else [settings.target_mesh]
        return [obj for obj in objects if obj and obj.type == 'MESH' and obj.data.shape_keys
                and settings.shape_key in obj.data.shape_keys.key_blocks
                and obj.data.shape_keys.is_editable]

    @staticmethod
    def retrieve_contacts(settings):
        if settings.contact_object:
            roots = [settings.contact_object]
        elif settings.contact_collection:
            members = set(settings.contact_collection.all_objects)
            roots = [obj for obj in members if obj.parent not in members]
        else:
            roots = []
        return roots

    @staticmethod
    def retrieve_direction(root, graph, receiver=None):
        scene = bpy.context.scene
        binding = POSITIONING.resolve_binding(root, scene, receiver)
        if binding:
            return POSITIONING.retrieve_entry_direction(binding, graph)
        evaluated = root.evaluated_get(graph)
        transform = evaluated.matrix_world
        bone_name = root.interactable_direction_bone
        if evaluated.type == 'ARMATURE' and bone_name in evaluated.pose.bones:
            transform = transform @ evaluated.pose.bones[bone_name].matrix
        return transform.to_3x3() @ Vector(root.interactable_entry_direction)

    @staticmethod
    def retrieve_contact_objects(root, scene, graph, excluded):
        binding = POSITIONING.resolve_binding(root, scene)
        if binding:
            return [binding.rig]
        return [contact for contact in [root, *root.children_recursive]
                if contact.type == 'MESH' and contact not in excluded
                and contact.name in scene.objects
                and contact.visible_get(view_layer=graph.view_layer)]

    @staticmethod
    def retrieve_contact_mesh(contact, root, scene, graph):
        binding = POSITIONING.resolve_binding(root, scene)
        if binding and contact == binding.rig:
            if len(binding.shaft_bones) == 1:
                return ContactMesh.shaft_from_bone(
                    binding.rig, binding.shaft_bones[0], graph, radius=binding.shaft_radius)
            return ContactMesh.shafts_from_bones(
                binding.rig, binding.shaft_bones, graph, radius=binding.shaft_radius)
        return ContactMesh.from_object(contact, graph)

    def refresh(self, scene, graph):
        if not self.busy and not self.suspended:
            self.busy = True
            try:
                if self.uses_fast_mode(scene, graph):
                    self._refresh_fast_preview(scene, graph)
                else:
                    self._refresh_full(scene, graph)
            finally:
                self.busy = False

    def _refresh_full(self, scene, graph):
        POSITIONING.synchronize(scene, graph)
        targets, snapshots, status, contacts, descendants = {}, {}, {}, {}, {}
        for obj in self.retrieve_receivers(scene):
            settings = obj.interactable
            meshes = self.retrieve_targets(settings)
            diameter, intersecting = 0.0, False
            matrix = obj.evaluated_get(graph).matrix_world
            available = (settings.enabled and meshes and abs(matrix.determinant()) > 1e-12
                         and any(mesh.visible_get(view_layer=graph.view_layer) for mesh in meshes))
            if available:
                region = ReceivingCylinder(matrix, settings.diameter, settings.height, settings.resolution)
                for root in self.retrieve_contacts(settings):
                    measurement = ContactMeasurement()
                    direction = self.retrieve_direction(root, graph, obj)
                    if root not in descendants:
                        descendants[root] = self.retrieve_contact_objects(root, scene, graph, meshes)
                    for contact in descendants[root]:
                        configuration = (tuple(value for row in matrix for value in row),
                                         settings.diameter, settings.height, settings.resolution,
                                         tuple(direction), contact.name)
                        token = (obj, contact)
                        previous = self.contacts.get(token)
                        if contact not in snapshots:
                            try:
                                snapshots[contact] = self.retrieve_contact_mesh(contact, root, scene, graph)
                            except Exception:
                                continue
                        snapshot = snapshots[contact]
                        if previous and previous[0] == configuration and snapshot.matches(previous[1]):
                            measured = previous[2]
                        else:
                            if region.overlaps_bounds(snapshot.vertices):
                                measured = self.measurement.measure(region, snapshot, direction)
                            else:
                                measured = ContactMeasurement()
                        contacts[token] = (configuration, snapshot, measured)
                        measurement.include(measured)
                    intersecting |= measurement.intersecting
                    diameter = max(diameter, measurement.retrieve_diameter())
                if intersecting:
                    value = max(settings.default_value, min(settings.maximum_value,
                                                            diameter * settings.diameter_scale))
                    for mesh in meshes:
                        key = mesh.data.shape_keys.key_blocks[settings.shape_key]
                        targets[key] = max(targets.get(key, value), value)
            status[obj.name] = (intersecting, diameter)
        self.response.apply(targets)
        self.status = status
        self.contacts = contacts

    def restore(self):
        self.busy = True
        try:
            self.response.restore()
            POSITIONING.restore_controls()
            self.status.clear()
        finally:
            self.busy = False


SYSTEM = InteractableSystem()


def refresh_preview(self, context):
    if context and context.scene:
        SYSTEM.refresh(context.scene, context.evaluated_depsgraph_get())
        context.view_layer.update()


def refresh_anatomy_object(self, context):
    """Rebind receivers when anatomy part or finger selection changes on a rig."""
    if context and context.scene and not SYSTEM.busy:
        for receiver in SYSTEM.retrieve_receivers(context.scene):
            settings = receiver.interactable
            if settings.contact_object is None:
                continue
            rig = POSITIONING.resolve_anatomy_rig(settings.contact_object, context.scene)
            if rig == self and settings.position_helper:
                POSITIONING.release(settings)
        self.update_tag()


def refresh_settings(self, context):
    if context and context.scene:
        if isinstance(self, InteractableSettings) and not SYSTEM.busy:
            SYSTEM.busy = True
            try:
                graph = context.evaluated_depsgraph_get()
                if self.position_helper and not SYSTEM.uses_fast_mode(context.scene, graph):
                    POSITIONING.update_transform(self)
                    if (self.position_owner
                            and self.position_owner.as_pointer() in POSITIONING.control_overrides):
                        POSITIONING.update_anatomy(self, graph)
            finally:
                SYSTEM.busy = False
        self.id_data.update_tag()


def _retrieve_action_slot(action, owner):
    if not action or not owner:
        return None
    for slot in getattr(action, "slots", []):
        if slot.target_id_type == owner.id_type and slot.name_display == owner.name:
            return slot
    animation = owner.animation_data
    if not animation:
        return None
    if animation.action == action and animation.action_slot:
        return animation.action_slot
    for track in animation.nla_tracks:
        for strip in track.strips:
            if strip.action == action and strip.action_slot:
                return strip.action_slot
    return None


def _retrieve_depth_curve(action, slot):
    if not action or not slot:
        return None
    for layer in action.layers:
        for strip in layer.strips:
            bag = strip.channelbag(slot)
            if bag is None:
                continue
            for curve in bag.fcurves:
                if curve.data_path == DEPTH_PATH and curve.array_index == 0:
                    return curve
    return None


def _retrieve_channelbag(action, slot):
    layer = action.layers[0] if action.layers else action.layers.new("Pose")
    strip = layer.strips[0] if layer.strips else layer.strips.new(type="KEYFRAME")
    bag = strip.channelbag(slot)
    if bag is None:
        bag = strip.channelbags.new(slot)
    return bag


def _action_frame_for_depth(receiver, action, scene_frame):
    animation = receiver.animation_data
    if animation and getattr(animation, "use_tweak_mode", False):
        try:
            return float(animation.nla_tweak_strip_time_to_scene(scene_frame, invert=True))
        except (TypeError, RuntimeError, ValueError):
            pass
    if animation:
        for track in animation.nla_tracks:
            for strip in track.strips:
                if strip.action != action:
                    continue
                scale = strip.scale if strip.scale else 1.0
                return float(strip.action_frame_start + (scene_frame - strip.frame_start) / scale)
    return float(scene_frame)


def key_position_depth(receiver, context):
    """Insert/update Depth at the current frame so panel edits stick on keyed clips.

    Respects auto-key when already on. When auto-key is off but Depth already has
    an fcurve on the active clip, still keys the current frame so the value does
    not snap back. Other frames (ping-pong OUT→IN) stay unchanged.
    """
    if _depth_key_suppress or SYSTEM.busy or SYSTEM.suspended:
        return False
    if receiver is None or context is None or context.scene is None:
        return False
    scene = context.scene
    action = None
    try:
        from animation_participants import retrieve_active_action
        action = retrieve_active_action(context)
    except Exception:
        action = None
    animation = receiver.animation_data
    candidates = []
    if action is not None and getattr(action, "is_editable", True):
        candidates.append(action)
    if animation and animation.action and getattr(animation.action, "is_editable", True):
        if animation.action not in candidates:
            candidates.append(animation.action)
    action = slot = None
    for candidate in candidates:
        found = _retrieve_action_slot(candidate, receiver)
        if found is not None:
            action, slot = candidate, found
            break
    if action is None or slot is None:
        return False
    curve = _retrieve_depth_curve(action, slot)
    auto_key = scene.tool_settings.use_keyframe_insert_auto
    if curve is None and not auto_key:
        return False
    value = float(receiver.interactable.position_depth)
    if animation and animation.action == action and animation.action_slot == slot:
        # Bound action / NLA tweakmode: Blender maps the scene frame into the strip.
        return bool(receiver.keyframe_insert(DEPTH_PATH))
    frame = _action_frame_for_depth(receiver, action, scene.frame_current)
    if curve is None:
        curve = _retrieve_channelbag(action, slot).fcurves.new(DEPTH_PATH, index=0)
    curve.keyframe_points.insert(frame, value)
    curve.update()
    try:
        curve.update_autoflags(receiver)
    except Exception:
        pass
    return True


def refresh_position_depth(self, context):
    refresh_settings(self, context)
    if isinstance(self, InteractableSettings):
        key_position_depth(self.id_data, context)


class InteractableSettings(bpy.types.PropertyGroup):
    is_receiver: bpy.props.BoolProperty(default=False)
    enabled: bpy.props.BoolProperty(name='Contact response', default=True, update=refresh_settings)
    target_mesh: bpy.props.PointerProperty(name='Target mesh', type=bpy.types.Object, update=refresh_settings)
    target_collection: bpy.props.PointerProperty(name='Target collection', type=bpy.types.Collection, update=refresh_settings)
    shape_key: bpy.props.StringProperty(name='Shape key', update=refresh_settings)
    contact_object: bpy.props.PointerProperty(name='Contact object', type=bpy.types.Object,
        description='Measure this object and its mesh descendants', update=refresh_settings)
    contact_collection: bpy.props.PointerProperty(name='Contact collection', type=bpy.types.Collection,
        description='Measure visible mesh hierarchies when the contact object field is empty', update=refresh_settings)
    auto_position: bpy.props.BoolProperty(name='Position automatically', default=True, update=refresh_settings)
    hand_contact: bpy.props.EnumProperty(name='Hand contact', default='FINGERTIPS',
        items=(('FINGERTIPS', 'Fingertips', 'Place the selected fingertips at the receiver'),
               ('PALM', 'Palm', 'Place the calibrated palm surface at the receiver')),
        update=refresh_settings)
    position_depth_maximum: bpy.props.FloatProperty(name='Maximum depth', default=0, min=0,
        subtype='DISTANCE', update=refresh_settings,
        description='Positive values limit contact travel in scene units; zero permits the authored Depth range')
    position_depth: bpy.props.FloatProperty(name='Depth', default=0, subtype='DISTANCE', update=refresh_position_depth,
        description='Tip displacement along the receiver positive Y axis, in scene units. Panel edits key the current frame when auto-key is on or Depth is already keyed on the active clip')
    position_tip: bpy.props.FloatVectorProperty(name='Local tip', size=3, subtype='TRANSLATION', update=refresh_settings,
        description='Contact point in the selected object local coordinates, calibrated when assigned')
    position_direction: bpy.props.FloatVectorProperty(size=3, default=(0, 0, 1))
    position_scale: bpy.props.FloatVectorProperty(size=3, default=(1, 1, 1))
    position_helper: bpy.props.PointerProperty(type=bpy.types.Object)
    position_owner: bpy.props.PointerProperty(type=bpy.types.Object)
    position_message: bpy.props.StringProperty()
    diameter: bpy.props.FloatProperty(name='Diameter', default=0.05, min=0.001, subtype='DISTANCE', update=refresh_settings)
    height: bpy.props.FloatProperty(name='Height', default=0.001, min=0.00001, subtype='DISTANCE', update=refresh_settings)
    default_value: bpy.props.FloatProperty(name='Minimum response', default=0, update=refresh_settings)
    maximum_value: bpy.props.FloatProperty(name='Maximum response', default=1, update=refresh_settings)
    diameter_scale: bpy.props.FloatProperty(name='Diameter scale', default=1, min=0, update=refresh_settings)
    resolution: bpy.props.IntProperty(name='Curve resolution', default=12, min=8, max=64, update=refresh_settings)


@persistent
def update_interactables(scene, graph):
    SYSTEM.refresh(scene, graph)


@persistent
def prepare_interactable_frame(scene, graph=None):
    # Restore the authored values before Blender evaluates this frame's animation.
    SYSTEM.suspended = True
    SYSTEM.restore()
    from animation_participants import retrieve_active_action
    from animation_interactables import apply_selection
    action = retrieve_active_action(bpy.context)
    if action and action.pose_markers.get('activity_start'):
        apply_selection(action, scene)


@persistent
def finish_interactable_frame(scene, graph):
    SYSTEM.suspended = False
    SYSTEM.refresh(scene, graph)


@persistent
def prepare_interactable_save(_):
    SYSTEM.suspended = True
    SYSTEM.restore()
    POSITIONING.release_fast_feet()


@persistent
def finish_interactable_save(_):
    SYSTEM.suspended = False
    SYSTEM.refresh(bpy.context.scene, bpy.context.evaluated_depsgraph_get())


@persistent
def restore_interactables(_):
    SYSTEM.response.values.clear()
    SYSTEM.status.clear()
    SYSTEM.contacts.clear()
    POSITIONING.control_overrides.clear()
    POSITIONING.ik_mode_overrides.clear()
    POSITIONING.foot_overrides.clear()
    POSITIONING.direction_overrides.clear()
    POSITIONING.palm_overrides.clear()
    PalmWristOverlay.clear_saved()
    POSITIONING.clear_fast_feet()
    SYSTEM.suspended = False


HANDLERS = {
    'depsgraph_update_post': update_interactables,
    'frame_change_pre': prepare_interactable_frame,
    'frame_change_post': finish_interactable_frame,
    'save_pre': prepare_interactable_save,
    'save_post': finish_interactable_save,
    'load_post': restore_interactables,
    'undo_post': restore_interactables,
    'redo_post': restore_interactables,
}


def register():
    if not hasattr(bpy.types.Scene, 'interactable_fast_mode'):
        bpy.types.Scene.interactable_fast_mode = bpy.props.BoolProperty(
            name='Fast mode', default=False, update=refresh_preview,
            description='Preview approximate positioning with contact deformation paused; '
                        'baking and export use full evaluation')
    if not hasattr(bpy.types.Object, 'interactable'):
        if not InteractableSettings.is_registered:
            bpy.utils.register_class(InteractableSettings)
        bpy.types.Object.interactable = bpy.props.PointerProperty(type=InteractableSettings)
        bpy.types.Object.interactable_entry_direction = bpy.props.FloatVectorProperty(
            name='Entry direction', default=(0, 0, 1), size=3, update=refresh_settings,
            description='Local direction from the trailing end toward the entering end')
        bpy.types.Object.interactable_direction_bone = bpy.props.StringProperty(
            name='Direction bone', update=refresh_settings,
            description='Optional armature bone whose posed axes define entry direction')
    if not hasattr(bpy.types.Object, 'interactable_anatomy_part'):
        bpy.types.Object.interactable_anatomy_part = bpy.props.EnumProperty(
            name='Contact hand',
            items=(
                ('AUTO', 'Auto', 'Choose an available hand'),
                ('HAND_L', 'Left hand', 'Selected left fingertips driven by hand_ik.L'),
                ('HAND_R', 'Right hand', 'Selected right fingertips driven by hand_ik.R'),
            ),
            default='AUTO',
            update=refresh_anatomy_object,
            description='Hand used for contact positioning on this rig')
    if not hasattr(bpy.types.Object, 'interactable_fingers'):
        bpy.types.Object.interactable_fingers = bpy.props.EnumProperty(
            name='Fingers',
            options={'ENUM_FLAG'},
            items=(
                ('THUMB', 'Thumb', 'Include thumb', 1),
                ('INDEX', 'Index', 'Include index finger', 2),
                ('MIDDLE', 'Middle', 'Include middle finger', 4),
                ('RING', 'Ring', 'Include ring finger', 8),
                ('PINKY', 'Pinky', 'Include pinky', 16),
            ),
            default={'THUMB', 'INDEX', 'MIDDLE', 'RING', 'PINKY'},
            update=refresh_anatomy_object,
            description='Fingers that define the hand tip and contact shafts')
    for name, callback in HANDLERS.items():
        handlers = getattr(bpy.app.handlers, name)
        for previous in list(handlers):
            if previous.__module__ == __name__:
                handlers.remove(previous)
        handlers.append(callback)


def unregister():
    SYSTEM.restore()
    POSITIONING.release_fast_feet()
    SYSTEM.contacts.clear()
    if hasattr(bpy.types.Scene, 'interactable_fast_mode'):
        del bpy.types.Scene.interactable_fast_mode
    for scene in bpy.data.scenes:
        for receiver in SYSTEM.retrieve_receivers(scene):
            if receiver.interactable.position_helper:
                POSITIONING.release(receiver.interactable)
    for name, callback in HANDLERS.items():
        handlers = getattr(bpy.app.handlers, name)
        if callback in handlers:
            handlers.remove(callback)
    for name in ('interactable', 'interactable_entry_direction', 'interactable_direction_bone',
                 'interactable_anatomy_part', 'interactable_fingers'):
        if hasattr(bpy.types.Object, name):
            delattr(bpy.types.Object, name)
    cls = bpy.types.PropertyGroup.bl_rna_get_subclass_py('InteractableSettings')
    if cls:
        bpy.utils.unregister_class(cls)
