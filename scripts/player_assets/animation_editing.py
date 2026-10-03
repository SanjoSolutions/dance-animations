"""Prepare the chosen animation's authoring strips and rigs for pose editing."""

from contextlib import contextmanager

import bpy

import animation_objects
import animation_participants
from animation_viewport import AnimationViewport


@contextmanager
def nla_editor(context):
    area = next((area for area in context.screen.areas if area.type == "NLA_EDITOR"), context.area)
    if area is None:
        area = context.screen.areas[0]
    previous_type = area.type
    area.type = "NLA_EDITOR"
    try:
        region = next(region for region in area.regions if region.type == "WINDOW")
        with context.temp_override(area=area, region=region):
            yield
    finally:
        area.type = previous_type


def finish_tweaking(context):
    if context.scene.is_nla_tweakmode:
        with nla_editor(context):
            bpy.ops.nla.tweakmode_exit()


class AnimationTrackEditor:
    def __init__(self, context):
        self.context = context

    def edit(self, name, focus=None):
        from track_chooser import TrackChooser
        from animation_creation import AnimationCreator
        from animation_object_editing import AnimationObjectEditor
        chooser = TrackChooser(self.context.scene)
        entries = chooser.retrieve_tracks()[name]
        action = animation_participants.retrieve_active_action(self.context)
        roles = {role for role in AnimationCreator.RIGS if animation_participants.includes(action, role)}
        objects = animation_objects.retrieve_selection(action)
        AnimationViewport.suspended += 1
        try:
            added_tracks = False
            if action and action.is_editable:
                for root, included in objects.items():
                    focused = focus is None or any(obj in focus for obj in [root, *root.children_recursive])
                    if included and focused:
                        added = AnimationObjectEditor(self.context).ensure_tracks(action, root, name, entries)
                        added_tracks = added_tracks or added
            if added_tracks:
                scene = self.context.scene
                frame, subframe = scene.frame_current, scene.frame_subframe
                chooser.apply(name)
                scene.frame_set(frame, subframe=subframe)
                entries = chooser.retrieve_tracks()[name]
        finally:
            AnimationViewport.suspended -= 1
        excluded = {self.context.scene.objects.get(rig) for role, rig in AnimationCreator.RIGS.items()
                    if role not in roles}
        excluded.update(obj for root, included in objects.items() if not included
                        for obj in [root, *root.children_recursive])
        source_actions = {strip.action for owner, track in entries for strip in track.strips
                          if strip.action and not strip.action.name.endswith((".baked", "_baked"))}
        editable = [(owner, track) for owner, track in entries if owner.is_editable and owner not in excluded
                    and (focus is None or owner in focus)
                    and any(strip.action and strip.action.is_editable
                            and (strip.action in source_actions or not source_actions) for strip in track.strips)]
        selected = []
        for owner, track in editable:
            if isinstance(owner, bpy.types.Object):
                selected.append(owner)
            else:
                selected.extend(obj for obj in self.context.scene.objects
                                if obj.type == "MESH" and obj.data.shape_keys == owner)
        AnimationViewport.suspended += 1
        try:
            finish_tweaking(self.context)
            AnimationViewport(self.context.view_layer).select_for_pose(selected)
            # The native operator processes selected strips across visible animation owners.
            for tracks in TrackChooser(self.context.scene).retrieve_tracks().values():
                for owner, track in tracks:
                    track.select = False
                    for strip in track.strips:
                        strip.select = False
            for owner, track in editable:
                owner.animation_data.nla_tracks.active = track
                track.select = True
                clips = [strip for strip in track.strips if strip.type == "CLIP" and strip.action
                         and strip.action.is_editable and (strip.action in source_actions or not source_actions)]
                if clips:
                    frame = self.context.scene.frame_current
                    strip = next((clip for clip in clips if clip.frame_start <= frame <= clip.frame_end), clips[0])
                    strip.select = True
            if editable:
                with nla_editor(self.context):
                    filters = self.context.space_data.dopesheet
                    selected_only, filter_text = filters.show_only_selected, filters.filter_text
                    try:
                        filters.show_only_selected = True
                        filters.filter_text = ""
                        result = bpy.ops.nla.tweakmode_enter(isolate_action=True)
                    finally:
                        filters.show_only_selected = selected_only
                        filters.filter_text = filter_text
                if result != {"FINISHED"}:
                    raise ValueError("Select an editable animation strip")
            self.context.view_layer.update()
        finally:
            AnimationViewport.suspended -= 1
