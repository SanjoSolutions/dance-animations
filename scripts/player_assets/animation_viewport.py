"""Viewport visibility for the characters and selectable animation objects."""

from contextlib import contextmanager

import bpy


class AnimationViewport:
    COLLECTIONS = {"PLAYER": "Man", "PARTNER": "Woman"}
    suspended = 0

    def __init__(self, view_layer):
        self.view_layer = view_layer
        self.collections = []
        self._collect(view_layer.layer_collection)

    def _collect(self, layer):
        for role, name in self.COLLECTIONS.items():
            if layer.collection.name == name:
                self.collections.append((role, layer))
        for child in layer.children:
            self._collect(child)

    def apply(self, participants, objects):
        for role, layer in self.collections:
            layer.hide_viewport = role not in participants
        for root, included in objects.items():
            for obj in [root, *root.children_recursive]:
                if obj.name in self.view_layer.objects:
                    obj.hide_set(not included, view_layer=self.view_layer)

    def select_for_pose(self, objects):
        objects = list(dict.fromkeys(objects))
        if bpy.context.mode != "OBJECT":
            bpy.ops.object.mode_set(mode="OBJECT")
        self._reveal_collections(self.view_layer.layer_collection, set(objects))
        self.view_layer.update()
        for obj in self.view_layer.objects:
            obj.select_set(False)
        for obj in objects:
            obj.hide_viewport = False
            obj.hide_set(False)
            obj.hide_select = False
            obj.select_set(True)
        rigs = [obj for obj in objects if obj.type == "ARMATURE"]
        if objects:
            self.view_layer.objects.active = (rigs or objects)[0]
            if rigs:
                bpy.ops.object.mode_set(mode="POSE")
        self.view_layer.update()

    def _reveal_collections(self, layer, objects):
        if objects.intersection(layer.collection.all_objects):
            layer.exclude = False
            layer.hide_viewport = False
            layer.collection.hide_viewport = False
            layer.collection.hide_select = False
            for child in layer.children:
                self._reveal_collections(child, objects)

    @contextmanager
    def reveal(self, objects):
        collections = [(layer, layer.hide_viewport) for role, layer in self.collections]
        members = {obj for root in objects for obj in [root, *root.children_recursive]
                   if obj.name in self.view_layer.objects}
        visibility = {obj: obj.hide_get(view_layer=self.view_layer) for obj in members}
        source_collections = {layer.collection for role, layer in self.collections}
        source_collections.update(collection for obj in members for collection in obj.users_collection)
        collection_visibility = {collection: collection.hide_viewport for collection in source_collections}
        AnimationViewport.suspended += 1
        try:
            for collection in source_collections:
                collection.hide_viewport = False
            self.apply(self.COLLECTIONS, dict.fromkeys(objects, True))
            yield
        finally:
            for layer, hidden in collections:
                layer.hide_viewport = hidden
            for obj, hidden in visibility.items():
                obj.hide_set(hidden, view_layer=self.view_layer)
            for collection, hidden in collection_visibility.items():
                collection.hide_viewport = hidden
            AnimationViewport.suspended -= 1


@contextmanager
def visible_animation_objects():
    from animation_objects import retrieve_objects
    with AnimationViewport(bpy.context.view_layer).reveal(retrieve_objects()):
        yield
