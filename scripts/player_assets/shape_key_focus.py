"""Switch object and pose context with the native animation editor mode."""

import bpy
from bpy.app.handlers import persistent


def is_shape_mesh(obj):
    return bool(obj and obj.type == "MESH" and obj.data.shape_keys)


def poll_shape_mesh(scene, obj):
    return is_shape_mesh(obj) and obj.name in scene.objects


class ShapeKeyFocus:
    def __init__(self):
        self.rig_name = ""
        self.rig_names = []

    def retrieve_mesh(self, context):
        active = context.view_layer.objects.active
        preferred = active if is_shape_mesh(active) else context.scene.shape_key_focus_mesh
        if preferred and preferred.name in context.view_layer.objects and preferred.visible_get():
            return preferred
        candidates = [obj for obj in context.view_layer.objects if is_shape_mesh(obj) and obj.visible_get()]
        candidates.sort(key=lambda obj: (not obj.data.shape_keys.is_editable, obj.name))
        return next(iter(candidates), None)

    def retrieve_rigs(self, context):
        from animation_participants import retrieve_active_action
        action = retrieve_active_action(context)
        slots = {slot.identifier for slot in action.slots} if action else set()
        rigs = [obj for obj in context.view_layer.objects
                if obj.type == "ARMATURE" and obj.visible_get() and obj.is_editable
                and "OB" + obj.name in slots]
        if not rigs:
            rigs = [obj for name in self.rig_names
                    if (obj := context.view_layer.objects.get(name)) and obj.visible_get() and obj.is_editable]
        if not rigs and context.object and context.object.type == "ARMATURE":
            rigs = [context.object]
        rigs.sort(key=lambda obj: (obj.name != self.rig_name, obj.name))
        return rigs

    def focus(self, context, editor_type):
        active = context.view_layer.objects.active
        if editor_type == "SHAPEKEY":
            if active and active.type == "ARMATURE":
                self.rig_name = active.name
            posed = [obj.name for obj in context.view_layer.objects
                     if obj.type == "ARMATURE" and obj.mode == "POSE" and obj.visible_get()]
            if posed:
                self.rig_names = posed
            if context.mode == "POSE":
                bpy.ops.object.mode_set(mode="OBJECT")
            mesh = self.retrieve_mesh(context)
            if mesh and context.mode == "OBJECT":
                context.scene.shape_key_focus_mesh = mesh
                for obj in context.view_layer.objects:
                    obj.select_set(False)
                mesh.select_set(True)
                context.view_layer.objects.active = mesh
                from shape_key_animation import ShapeKeyAnimation
                ShapeKeyAnimation().synchronize(context, mesh)
        elif editor_type in {"ACTION", "DOPESHEET"} and context.mode in {"OBJECT", "POSE"}:
            if is_shape_mesh(active):
                context.scene.shape_key_focus_mesh = active
            rigs = self.retrieve_rigs(context)
            if rigs:
                from animation_viewport import AnimationViewport
                AnimationViewport(context.view_layer).select_for_pose(rigs)
                self.rig_name = context.object.name
                self.rig_names = [rig.name for rig in rigs]


class EditorModeObserver:
    def __init__(self):
        self.modes = {}
        self.controllers = {}

    def synchronize(self, initialize=False):
        for window in bpy.context.window_manager.windows:
            controller = self.controllers.setdefault(window.as_pointer(), ShapeKeyFocus())
            for area in window.screen.areas:
                if area.type == "DOPESHEET_EDITOR":
                    mode = area.spaces.active.mode
                    identifier = (window.as_pointer(), area.as_pointer())
                    previous = self.modes.get(identifier)
                    self.modes[identifier] = mode
                    if not initialize and previous != mode and window.scene.shape_key_focus_enabled:
                        with bpy.context.temp_override(window=window, area=area):
                            controller.focus(bpy.context, mode)
                        for editor in window.screen.areas:
                            editor.tag_redraw()


_observer = EditorModeObserver()
_subscription_owner = object()
_registered = False
_synchronizing_selection = False
_previous_active = None


def synchronize_modes():
    if _registered:
        _observer.synchronize()



@persistent
def synchronize_selected_mesh(*args):
    """Keep the open animation on a shape mesh chosen while the Shape Key Editor is active."""
    global _synchronizing_selection, _previous_active
    if _synchronizing_selection or not _registered:
        return
    context = bpy.context
    scene = getattr(context, "scene", None)
    window = getattr(context, "window", None)
    objects = getattr(getattr(context, "view_layer", None), "objects", None)
    mesh = objects.active if objects else None
    pointer = mesh.as_pointer() if mesh else None
    if pointer == _previous_active:
        return
    _previous_active = pointer
    if scene is None or window is None or not getattr(scene, "shape_key_focus_enabled", False):
        return
    area = next((area for area in window.screen.areas
                 if area.type == "DOPESHEET_EDITOR" and area.spaces.active.mode == "SHAPEKEY"), None)
    if area is None or not poll_shape_mesh(scene, mesh) or not mesh.visible_get():
        return
    if scene.shape_key_focus_mesh == mesh:
        keys = mesh.data.shape_keys
        animation = keys.animation_data
        from animation_participants import retrieve_active_action
        action = retrieve_active_action(context)
        if action and animation and animation.action == action:
            return
    _synchronizing_selection = True
    try:
        scene.shape_key_focus_mesh = mesh
        with context.temp_override(window=window, area=area):
            from shape_key_animation import ShapeKeyAnimation
            ShapeKeyAnimation().synchronize(context, mesh)
    finally:
        _synchronizing_selection = False


def synchronize_animation(context):
    if context.scene.shape_key_focus_enabled:
        area = next((area for area in context.screen.areas
                     if area.type == "DOPESHEET_EDITOR" and area.spaces.active.mode == "SHAPEKEY"), None)
        if area:
            controller = _observer.controllers.setdefault(context.window.as_pointer(), ShapeKeyFocus())
            with context.temp_override(area=area):
                controller.focus(context, "SHAPEKEY")


def update_enabled(scene, context):
    if scene.shape_key_focus_enabled and context.area and context.area.type == "DOPESHEET_EDITOR":
        controller = _observer.controllers.setdefault(context.window.as_pointer(), ShapeKeyFocus())
        controller.focus(context, context.space_data.mode)


def subscribe():
    bpy.msgbus.clear_by_owner(_subscription_owner)
    for property_name in ("mode", "ui_mode"):
        bpy.msgbus.subscribe_rna(key=(bpy.types.SpaceDopeSheetEditor, property_name),
                                owner=_subscription_owner, args=(), notify=synchronize_modes)
    if synchronize_selected_mesh not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(synchronize_selected_mesh)
    _observer.synchronize(initialize=True)


@persistent
def restore_subscriptions(*args):
    global _observer, _previous_active
    _observer = EditorModeObserver()
    _previous_active = None
    subscribe()
    synchronize_animation(bpy.context)


def draw_header(self, context):
    if context.space_data.mode in {"SHAPEKEY", "ACTION", "DOPESHEET"}:
        row = self.layout.row(align=True)
        row.prop(context.scene, "shape_key_focus_enabled", text="Auto switch", toggle=True)
        if context.space_data.mode == "SHAPEKEY":
            row.prop(context.scene, "shape_key_focus_mesh", text="Mesh")


def update_mesh(scene, context):
    mesh = scene.shape_key_focus_mesh
    if scene.shape_key_focus_enabled and mesh and context.mode == "OBJECT":
        if context.area and context.area.type == "DOPESHEET_EDITOR" and context.space_data.mode == "SHAPEKEY":
            mesh.select_set(True)
            context.view_layer.objects.active = mesh
            from shape_key_animation import ShapeKeyAnimation
            ShapeKeyAnimation().synchronize(context, mesh)


def register():
    global _registered
    if not _registered:
        bpy.types.Scene.shape_key_focus_enabled = bpy.props.BoolProperty(
            name="Auto switch", default=False, update=update_enabled,
            description="Use Object Mode in the Shape Key Editor and Pose Mode in the Action Editor or Dope Sheet")
        bpy.types.Scene.shape_key_focus_mesh = bpy.props.PointerProperty(
            name="Mesh", type=bpy.types.Object, poll=poll_shape_mesh, update=update_mesh,
            description="Mesh to activate when entering the Shape Key Editor")
        bpy.types.DOPESHEET_HT_header.append(draw_header)
        bpy.app.handlers.load_post.append(restore_subscriptions)
        _registered = True
        subscribe()


def unregister():
    global _registered
    _registered = False
    bpy.msgbus.clear_by_owner(_subscription_owner)
    if synchronize_selected_mesh in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(synchronize_selected_mesh)
    bpy.app.handlers.load_post.remove(restore_subscriptions)
    bpy.types.DOPESHEET_HT_header.remove(draw_header)
    del bpy.types.Scene.shape_key_focus_mesh
    del bpy.types.Scene.shape_key_focus_enabled
