"""Keep animation evaluation focused on motion after gathering mesh geometry."""

import bpy


class AnimationExportEvaluation:
    def __init__(self, objects):
        self.objects = set(objects)
        self.modifiers = []
        self.hidden = []

    def prepare(self):
        users = bpy.data.user_map()
        scene = bpy.context.scene
        physics = (scene.rigidbody_world is not None or any(
            modifier.type in {"CLOTH", "SOFT_BODY", "FLUID", "DYNAMIC_PAINT", "COLLISION"}
            for obj in scene.objects for modifier in obj.modifiers))
        if physics:
            return
        if not (scene.animation_data and scene.animation_data.drivers):
            dependencies = {}
            for dependency, owners in users.items():
                for owner in owners:
                    dependencies.setdefault(owner, set()).add(dependency)
            required = set()
            pending = set(self.objects)
            while pending:
                owner = pending.pop()
                required.add(owner)
                pending.update(dependencies.get(owner, set()) - required)
            for obj in scene.objects:
                if obj not in required and not obj.hide_viewport:
                    self.hidden.append(obj)
                    obj.hide_viewport = True
        for obj in bpy.context.scene.objects:
            # Leaf meshes supply their geometry before sampling. Their skinning
            # and subdivision affect vertices, while tracks use transforms and
            # shape weights. Referenced meshes retain their evaluated surfaces
            # for constraints, drivers, parenting and geometry nodes.
            if obj.type == "MESH" and self._has_scene_users(obj, users, set()):
                for modifier in obj.modifiers:
                    if modifier.type in {"ARMATURE", "SUBSURF"} and modifier.show_viewport:
                        self.modifiers.append(modifier)
                        modifier.show_viewport = False

    def _has_scene_users(self, owner, users, visited):
        visited.add(owner)
        for user in users.get(owner, ()):
            if user not in visited:
                if isinstance(user, bpy.types.Collection):
                    if not self._has_scene_users(user, users, visited):
                        return False
                elif (not isinstance(user, bpy.types.Scene)
                      or (user.animation_data and user.animation_data.drivers)):
                    return False
        return True

    def restore(self):
        for obj in self.hidden:
            obj.hide_viewport = False
        self.hidden.clear()
        for modifier in self.modifiers:
            modifier.show_viewport = True
        self.modifiers.clear()
