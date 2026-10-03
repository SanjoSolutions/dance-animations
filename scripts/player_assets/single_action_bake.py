"""Bake one authoring action through Game Rig Tools while retaining editor state."""

from contextlib import contextmanager
import time

import bpy

from animation_export_evaluation import AnimationExportEvaluation
from interactable import SYSTEM


class SingleActionBake:
    def __init__(self, bakery, rigs):
        self.bakery = bakery
        self.rigs = rigs

    def retrieve_actions(self):
        actions = {item.Action for item in bpy.context.scene.GRT_Action_Bakery if item.Action}
        for source, target in self.bakery.get_rig_pairs(bpy.context):
            animation = source.animation_data
            if animation:
                if animation.action:
                    actions.add(animation.action)
                actions.update(strip.action for track in animation.nla_tracks for strip in track.strips if strip.action)
        return {action.name: action for action in actions if not action.name.endswith((".baked", "_baked"))}

    def retrieve_active(self):
        obj = bpy.context.object
        animation = obj.animation_data if obj else None
        action = animation.action if animation else None
        if action is None and animation and animation.nla_tracks.active:
            strips = animation.nla_tracks.active.strips
            if len(strips) == 1:
                action = strips[0].action
        result = None
        if action:
            if action.name in self.retrieve_actions():
                result = action.name
            else:
                matches = {item.Action.name for item in bpy.context.scene.GRT_Action_Bakery
                           if item.Action and self.bakery.Change_to_Baked_Name(bpy.context, item) == action.name}
                matches.update(name for name in self.retrieve_actions()
                               if action.name in {name + ".baked", name + "_baked"})
                if len(matches) == 1:
                    result = matches.pop()
        return result

    @SYSTEM.full_evaluation()
    def bake(self, name):
        started = time.perf_counter()
        pairs = self.bakery.get_rig_pairs(bpy.context)
        if {target for source, target in pairs} != set(self.rigs):
            raise RuntimeError("Enable both player rig pairs in Action Bakery before exporting")
        action = self.retrieve_actions().get(name)
        if action is None:
            raise RuntimeError("Choose an authoring action on a configured control rig")
        scene = bpy.context.scene
        settings = scene.GRT_Action_Bakery_Global_Settings
        if settings.BAKE_SETTINGS_Do_Constraint_Clear or settings.BAKE_SETTINGS_Do_Parent_Clear:
            raise RuntimeError("Keep constraints and parents in Action Bakery for repeatable clip updates")
        item = next((item for item in scene.GRT_Action_Bakery if item.Action == action), None)
        if item is None:
            bpy.ops.gamerigtool.action_bakery_list_operator(operation="ADD", action=name)
            item = next(item for item in scene.GRT_Action_Bakery if item.Action == action)
            item.Set_FR_Start = int(action.frame_range[0])
            item.Set_FR_End = int(action.frame_range[1])
        baked_name = self.bakery.Change_to_Baked_Name(bpy.context, item)
        if baked_name == name or not baked_name.endswith((".baked", "_baked")):
            raise RuntimeError(f"Set a distinct .baked or _baked output name for {name}")
        selected = [(entry, entry.Bake_Select) for entry in scene.GRT_Action_Bakery]
        overrides = dict(Push_to_NLA=True, Pre_Unmute_Constraint=True, Post_Mute_Constraint=False,
                         Overwrite=True, BAKE_SETTINGS_Only_Selected=False,
                         BAKE_SETTINGS_Do_Pose=True, BAKE_SETTINGS_Do_Visual_Keying=True)
        saved_settings = {key: getattr(settings, key) for key in overrides}
        evaluation = AnimationExportEvaluation({rig for pair in pairs for rig in pair})
        try:
            for entry, value in selected:
                entry.Bake_Select = entry == item
            for key, value in overrides.items():
                setattr(settings, key, value)
            with self._preserve_context(pairs):
                evaluation.prepare()
                try:
                    result = bpy.ops.gamerigtool.bake_action_bakery()
                    if result != {"FINISHED"}:
                        raise RuntimeError(f"Action Bakery failed while baking {name}")
                finally:
                    evaluation.restore()
        finally:
            for entry, value in selected:
                entry.Bake_Select = value
            for key, value in saved_settings.items():
                setattr(settings, key, value)
        import animation_objects
        baked = bpy.data.actions.get(baked_name)
        if baked:
            animation_objects.copy_choices(action, baked)
        print(f"Baked {name} in {time.perf_counter() - started:.2f} seconds", flush=True)
        return baked_name

    @contextmanager
    def _preserve_context(self, pairs):
        context = bpy.context
        active = context.view_layer.objects.active
        selected = set(context.selected_objects)
        mode = context.object.mode if context.object else "OBJECT"
        frame, subframe = context.scene.frame_current, context.scene.frame_subframe
        visibility = {rig: (rig.hide_viewport, rig.hide_get()) for pair in pairs for rig in pair}
        constraints = [(constraint, constraint.mute) for source, target in pairs
                       for bone in target.pose.bones for constraint in bone.constraints]
        if context.mode != "OBJECT":
            bpy.ops.object.mode_set(mode="OBJECT")
        try:
            yield
        finally:
            for constraint, muted in constraints:
                constraint.mute = muted
            for rig in visibility:
                rig.hide_viewport = False
                rig.hide_set(False)
            for obj in context.view_layer.objects:
                obj.select_set(obj in selected)
            context.view_layer.objects.active = active
            for rig, (viewport, hidden) in visibility.items():
                rig.hide_set(hidden)
                rig.hide_viewport = viewport
            context.scene.frame_set(frame, subframe=subframe)
            if mode != "OBJECT":
                bpy.ops.object.mode_set(mode=mode)
