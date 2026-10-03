"""Per-action checkboxes for object hierarchies in the Dance props collection."""

import re

import bpy
from bpy.app.handlers import persistent


_BAKED_SUFFIXES = (".baked", "_baked")
_DANCE_PROP_RULES = ()


def retrieve_objects():
    collection = bpy.data.collections.get("Dance props")
    members = set(collection.all_objects) if collection else set()
    return sorted((obj for obj in members if obj.parent not in members), key=lambda obj: obj.name)


def retrieve_label(obj):
    meshes = [child for child in obj.children_recursive if child.type == "MESH"]
    return meshes[0].name if obj.type == "ARMATURE" and len(meshes) == 1 else obj.name


def retrieve_base_name(name):
    for suffix in _BAKED_SUFFIXES:
        if name.endswith(suffix):
            return name[:-len(suffix)]
    return name


def retrieve_required_names(action_name):
    """Prop root names this clip should enable; empty means all Dance props off."""
    base = retrieve_base_name(action_name)
    for pattern, names in _DANCE_PROP_RULES:
        if pattern.search(base):
            return set(names)
    return set()


def retrieve_selection(action):
    from animation_files import retrieve_choice_object
    register_properties()
    entries = action.animation_objects if action else []
    choices = {retrieve_choice_object(choice): bool(choice.included) for choice in entries}
    return {obj: choices.get(obj, False) for obj in retrieve_objects()}


def apply_selection(action, included_names):
    """Set Dance props checkboxes from a set/list of root object names that should stay on."""
    if not action:
        return
    wanted = set(included_names)
    synchronize_choices(action)
    for choice in action.animation_objects:
        choice.included = bool(choice.object and choice.object.name in wanted)


def prune_to_required(action):
    """Enable only props inferred from the action name; turn the rest off."""
    apply_selection(action, retrieve_required_names(action.name))


def copy_choices(source, target):
    """Copy Dance props checkboxes from an authoring action onto its baked twin."""
    if not source or not target or source == target:
        return
    synchronize_choices(source)
    synchronize_choices(target)
    selection = retrieve_selection(source)
    for choice in target.animation_objects:
        choice.included = selection.get(choice.object, False)


def update_choice(choice, context):
    from animation_participants import retrieve_active_action, update_preview
    from animation_viewport import AnimationViewport
    action = choice.id_data
    if not AnimationViewport.suspended and action == retrieve_active_action(context):
        from animation_object_editing import AnimationObjectEditor
        AnimationObjectEditor(context).apply(action, choice.object, choice.included)
    update_preview(action, context)


class AnimationObjectChoice(bpy.types.PropertyGroup):
    object: bpy.props.PointerProperty(type=bpy.types.Object)
    included: bpy.props.BoolProperty(name="Included", default=False, update=update_choice)


def synchronize_choices(action):
    from animation_files import retrieve_choice_object
    if action and action.is_editable:
        existing = {retrieve_choice_object(choice) for choice in action.animation_objects}
        for choice in action.animation_objects:
            if choice.object is None:
                choice.object = retrieve_choice_object(choice)
        for obj in retrieve_objects():
            if obj not in existing:
                choice = action.animation_objects.add()
                choice.object = obj
                choice.included = False


_synchronizing = False
_previous = None


@persistent
def synchronize_preview(*args):
    global _synchronizing, _previous
    from animation_participants import retrieve_active_action, retrieve_selection as retrieve_participants, update_preview
    from animation_viewport import AnimationViewport
    from animation_wrist_constraints import retrieve_enabled
    import animation_interactables
    if getattr(bpy.context, "scene", None) and not _synchronizing and not AnimationViewport.suspended:
        _synchronizing = True
        try:
            action = retrieve_active_action(bpy.context)
            objects = retrieve_objects()
            synchronize_choices(action)
            animation_interactables.synchronize_choices(action)
            selection = (action, retrieve_participants(action), tuple(retrieve_selection(action).items()),
                         retrieve_enabled(action), animation_interactables.retrieve_signature(action),
                         bpy.context.view_layer)
            if selection != _previous:
                _previous = selection
                update_preview(action, bpy.context)
        finally:
            _synchronizing = False


def register_properties():
    if not hasattr(bpy.types.Action, "animation_objects"):
        bpy.utils.register_class(AnimationObjectChoice)
        bpy.types.Action.animation_objects = bpy.props.CollectionProperty(type=AnimationObjectChoice)


def register():
    register_properties()
    if not bpy.app.background:
        for handlers in (bpy.app.handlers.depsgraph_update_post, bpy.app.handlers.load_post, bpy.app.handlers.undo_post):
            if synchronize_preview not in handlers:
                handlers.append(synchronize_preview)
        synchronize_preview()


def unregister():
    for handlers in (bpy.app.handlers.depsgraph_update_post, bpy.app.handlers.load_post, bpy.app.handlers.undo_post):
        if synchronize_preview in handlers:
            handlers.remove(synchronize_preview)
    del bpy.types.Action.animation_objects
    bpy.utils.unregister_class(AnimationObjectChoice)
