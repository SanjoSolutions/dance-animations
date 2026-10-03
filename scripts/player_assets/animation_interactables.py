"""Per-action Interactable receiver enabled state and contact object."""

import bpy

from interactable import SYSTEM, InteractableSystem
from interactable_positioning import POSITIONING


_applying = False
_deferred = False


def update_choice(choice, context):
    from animation_participants import retrieve_active_action, update_preview
    from animation_viewport import AnimationViewport
    action = choice.id_data
    if not AnimationViewport.suspended and action == retrieve_active_action(context):
        apply_selection(action, context.scene)
    update_preview(action, context)


class AnimationInteractableChoice(bpy.types.PropertyGroup):
    receiver: bpy.props.PointerProperty(type=bpy.types.Object)
    enabled: bpy.props.BoolProperty(name="Contact response", default=False, update=update_choice)
    contact_object: bpy.props.PointerProperty(
        name="Contact object", type=bpy.types.Object,
        description="Measure this object and its mesh descendants for this animation",
        update=update_choice)
    auto_position: bpy.props.BoolProperty(
        name="Position automatically", default=True, update=update_choice)


def _deferred_register():
    global _deferred
    _deferred = False
    register_properties()
    window_manager = bpy.context.window_manager
    if window_manager:
        for window in window_manager.windows:
            for area in window.screen.areas:
                area.tag_redraw()
    return None


def synchronize_choices(action, scene=None):
    from animation_files import retrieve_choice_object
    if not action:
        return False
    if not register_properties():
        return False
    scene = scene or bpy.context.scene
    existing = {retrieve_choice_object(choice, "receiver", scene) for choice in action.animation_interactables}
    for receiver in InteractableSystem.retrieve_receivers(scene):
        if action.is_editable and receiver not in existing:
            choice = action.animation_interactables.add()
            choice.receiver = receiver
    return True


def retrieve_selection(action, scene=None):
    from animation_files import retrieve_choice_object
    register_properties()
    scene = scene or bpy.context.scene
    entries = {retrieve_choice_object(choice, "receiver", scene): choice
               for choice in (action.animation_interactables if action else [])
               if retrieve_choice_object(choice, "receiver", scene)} if action and hasattr(action, "animation_interactables") else {}
    result = {}
    for receiver in InteractableSystem.retrieve_receivers(scene):
        choice = entries.get(receiver)
        if choice:
            result[receiver] = (bool(choice.enabled), retrieve_choice_object(choice, "contact_object", scene),
                                bool(choice.auto_position))
        else:
            result[receiver] = (False, None, True)
    return result


def retrieve_signature(action, scene=None):
    return tuple(
        (receiver.name, enabled, contact.name if contact else "", auto)
        for receiver, (enabled, contact, auto) in sorted(
            retrieve_selection(action, scene).items(), key=lambda item: item[0].name))


def apply_selection(action, scene):
    global _applying
    if _applying:
        return
    if not register_properties():
        return
    _applying = True
    try:
        selection = retrieve_selection(action, scene)
        from animation_phase_markers import AnimationPhaseMarkers
        markers = AnimationPhaseMarkers(action).retrieve() if action else {}
        activity_frame = not markers or markers["activity_start"] <= scene.frame_current_final <= markers["activity_end"]
        for receiver in InteractableSystem.retrieve_receivers(scene):
            enabled, contact, auto_position = selection.get(receiver, (False, None, True))
            enabled = enabled and activity_frame
            settings = receiver.interactable
            if settings.enabled != enabled:
                settings.enabled = enabled
            if settings.contact_object != contact:
                settings.contact_object = contact
            if settings.auto_position != auto_position:
                settings.auto_position = auto_position
            if not enabled or contact is None:
                if settings.position_helper:
                    POSITIONING.release(settings)
        receiver_names = {receiver.name for receiver in selection}
        SYSTEM.status = {name: value for name, value in SYSTEM.status.items() if name in receiver_names}
    finally:
        _applying = False


def capture_live(action, scene=None):
    """Store the scene receivers' current enabled/object choices onto the action."""
    if not register_properties():
        return
    scene = scene or bpy.context.scene
    synchronize_choices(action, scene)
    for choice in action.animation_interactables:
        receiver = choice.receiver
        if receiver:
            settings = receiver.interactable
            choice.enabled = settings.enabled
            choice.contact_object = settings.contact_object
            choice.auto_position = settings.auto_position


def register_properties():
    """Attach Action.animation_interactables. Safe to call from draw (no write if present)."""
    global _deferred
    try:
        bpy.utils.register_class(AnimationInteractableChoice)
    except ValueError:
        pass
    if hasattr(bpy.types.Action, "animation_interactables"):
        return True
    try:
        bpy.types.Action.animation_interactables = bpy.props.CollectionProperty(
            type=AnimationInteractableChoice)
        return True
    except AttributeError:
        # Panel draw / depsgraph evaluation is RNA read-only; finish registration next tick.
        if not bpy.app.background and not _deferred and not bpy.app.timers.is_registered(_deferred_register):
            _deferred = True
            bpy.app.timers.register(_deferred_register, first_interval=0.0)
        return False


def register():
    register_properties()


def unregister():
    global _deferred
    if bpy.app.timers.is_registered(_deferred_register):
        bpy.app.timers.unregister(_deferred_register)
    _deferred = False
    if hasattr(bpy.types.Action, "animation_interactables"):
        del bpy.types.Action.animation_interactables
    try:
        bpy.utils.unregister_class(AnimationInteractableChoice)
    except RuntimeError:
        pass
