"""Export a baked rig clip in the open Blender session using a small temporary scene."""

from contextlib import contextmanager
import sys
from types import ModuleType

import bmesh
import bpy

from animation_export_tracks import AnimationExportTracks, retrieve_animation_owners


class AnimationClipScene:
    def __init__(self, rigs, objects):
        self.rigs = rigs
        self.objects = objects
        self.created = []
        self.copies = {}

    @contextmanager
    def activate(self, name):
        window = bpy.context.window
        original = window.scene
        module_name = "player_assets_single_clip"
        addon = None
        try:
            scene = bpy.data.scenes.new("Player clip export")
            self.created.append(scene)
            scene.render.fps = original.render.fps
            scene.render.fps_base = original.render.fps_base
            scene.frame_current = original.frame_current
            self._populate(scene, name)
            names = {copy: obj.name for obj, copy in self.copies.items()}

            class ClipNames:
                def gather_node_name_hook(self, hook, obj, settings):
                    hook.name = names.get(obj, obj.name)

            module = ModuleType(module_name)
            module.glTF2ExportUserExtension = ClipNames
            sys.modules[module_name] = module
            addon = bpy.context.preferences.addons.new()
            addon.module = module_name
            window.scene = scene
            for obj in scene.objects:
                obj.select_set(True)
            bpy.context.view_layer.objects.active = self.copies[self.rigs[0]]
            yield
        finally:
            window.scene = original
            if addon:
                bpy.context.preferences.addons.remove(addon)
            sys.modules.pop(module_name, None)
            bpy.data.batch_remove(ids=self.created)

    def _populate(self, scene, name):
        for obj in self.objects:
            if obj.type in {"ARMATURE", "EMPTY"}:
                copy = obj.copy()
                self.created.append(copy)
                if obj.type == "ARMATURE":
                    copy.data = obj.data.copy()
                    self.created.append(copy.data)
                    copy.data.pose_position = "POSE"
                    for bone in copy.pose.bones:
                        if obj in self.rigs:
                            for constraint in list(bone.constraints):
                                bone.constraints.remove(constraint)
                        bone.custom_shape = None
                scene.collection.objects.link(copy)
                copy.hide_viewport = False
                copy.hide_render = False
                copy.hide_select = False
                self.copies[obj] = copy
        for obj in self.objects:
            # Mesh names participate in Godot's bone-name resolution. Keep their
            # hierarchy with tiny geometry, including meshes sharing bone names.
            if obj.type == "MESH":
                self._add_mesh_marker(scene, obj)
        self._remap_shape_drivers()
        props = bpy.data.objects.new("AnimationProps", None)
        self.created.append(props)
        scene.collection.objects.link(props)
        for original, copy in self.copies.items():
            copy.parent = self.copies.get(original.parent, None if original in self.rigs else props)
        tracks = AnimationExportTracks([self.copies[rig] for rig in self.rigs])
        for obj in self.copies.values():
            for owner in retrieve_animation_owners(obj):
                tracks.prepare(owner)
                if owner.animation_data:
                    for track in list(owner.animation_data.nla_tracks):
                        if track.name != name:
                            owner.animation_data.nla_tracks.remove(track)
            if obj.type == "ARMATURE":
                self._add_skin_marker(scene, obj)

    def _add_skin_marker(self, scene, rig):
        # A triangle tells the standard exporter which nodes are skin joints.
        # Only its animation channels are copied into the existing GLB.
        mesh = self._create_marker_mesh()
        marker = bpy.data.objects.new("Player clip skin", mesh)
        self.created.append(marker)
        scene.collection.objects.link(marker)
        marker.parent = rig
        group = marker.vertex_groups.new(name=rig.data.bones[0].name)
        group.add([0, 1, 2], 1, "REPLACE")
        marker.modifiers.new("Skin", "ARMATURE").object = rig

    def _create_marker_mesh(self):
        mesh = bpy.data.meshes.new("Player clip skin")
        self.created.append(mesh)
        mesh.from_pydata([(0, 0, 0), (0.001, 0, 0), (0, 0.001, 0)], [], [(0, 1, 2)])
        return mesh

    def _add_mesh_marker(self, scene, original):
        marker = original.copy()
        self.created.append(marker)
        marker.data = self._create_shape_marker_mesh(original) if original.data.shape_keys else self._create_marker_mesh()
        marker.hide_viewport = False
        marker.hide_render = False
        marker.hide_select = False
        scene.collection.objects.link(marker)
        for modifier in list(marker.modifiers):
            if modifier.type == "ARMATURE" and modifier.object in self.copies:
                modifier.object = self.copies[modifier.object]
                bone = modifier.object.data.bones[0].name
                group = marker.vertex_groups.get(bone) or marker.vertex_groups.new(name=bone)
                group.add([0, 1, 2], 1, "REPLACE")
            else:
                marker.modifiers.remove(modifier)
        self.copies[original] = marker

    def _remap_shape_drivers(self):
        targets = dict(self.copies)
        targets.update({original.data.shape_keys: copy.data.shape_keys
                        for original, copy in self.copies.items()
                        if original.type == "MESH" and original.data.shape_keys})
        # Resolve dependencies after every mesh has its temporary counterpart.
        for copy in self.copies.values():
            if copy.type == "MESH" and copy.data.shape_keys and copy.data.shape_keys.animation_data:
                for curve in copy.data.shape_keys.animation_data.drivers:
                    for variable in curve.driver.variables:
                        for target in variable.targets:
                            if target.id in targets:
                                target.id = targets[target.id]

    def _create_shape_marker_mesh(self, original):
        # Copying the mesh retains shape actions, slots, NLA settings and drivers.
        mesh = original.data.copy()
        self.created.extend([mesh, mesh.shape_keys])
        mesh.materials.clear()
        geometry = bmesh.new()
        try:
            geometry.from_mesh(mesh)
            bmesh.ops.delete(geometry, geom=list(geometry.verts), context="VERTS")
            vertices = [geometry.verts.new(position) for position in
                        [(0, 0, 0), (0.001, 0, 0), (0, 0.001, 0)]]
            geometry.faces.new(vertices)
            for layer in geometry.verts.layers.shape.values():
                for vertex in vertices:
                    vertex[layer] = vertex.co
            geometry.to_mesh(mesh)
        finally:
            geometry.free()
        return mesh
