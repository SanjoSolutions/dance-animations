"""Connect object inclusion choices to editable animation tracks and pose selection."""

from animation_creation import PoseChannels
from animation_editing import AnimationTrackEditor, finish_tweaking
from animation_viewport import AnimationViewport
from track_chooser import TrackChooser


class AnimationObjectEditor:
    def __init__(self, context):
        self.context = context

    def apply(self, action, root, included):
        chooser = TrackChooser(self.context.scene)
        name = chooser.retrieve_active_name()
        if name and root and action.is_editable:
            scene = self.context.scene
            frame, subframe = scene.frame_current, scene.frame_subframe
            start, end = scene.frame_start, scene.frame_end
            AnimationViewport.suspended += 1
            try:
                if included:
                    self.ensure_tracks(action, root, name, chooser.retrieve_tracks()[name])
                finish_tweaking(self.context)
                chooser.apply(name)
                scene.frame_start, scene.frame_end = start, end
                scene.frame_set(frame, subframe=subframe)
                AnimationTrackEditor(self.context).edit(name)
                scene.tool_settings.use_keyframe_insert_auto = True
            finally:
                AnimationViewport.suspended -= 1

    def ensure_tracks(self, action, root, name, entries):
        objects = [root, *root.children_recursive]
        shapes = [obj.data.shape_keys for obj in objects if obj.type == "MESH" and obj.data.shape_keys]
        owners = list(dict.fromkeys([*objects, *shapes]))
        owners = [owner for owner in owners if owner.is_editable and not (
            owner.animation_data and any(track.name == name and track.strips
                                        for track in owner.animation_data.nla_tracks))]
        templates = [strip for owner, track in entries for strip in track.strips if strip.action == action]
        template = max(templates, key=lambda strip: strip.frame_end - strip.frame_start, default=None)
        with AnimationViewport(self.context.view_layer).reveal([root]):
            self.context.view_layer.update()
            snapshots = [PoseChannels(owner) for owner in owners]
        if snapshots:
            finish_tweaking(self.context)
        for snapshot in snapshots:
            owner = snapshot.owner
            animation = owner.animation_data_create()
            slots = [strip.action_slot for track in animation.nla_tracks for strip in track.strips
                     if strip.action == action and strip.action_slot]
            if animation.action == action and animation.action_slot:
                slots.append(animation.action_slot)
            slots.extend(slot for slot in action.slots
                         if slot.target_id_type == owner.id_type and slot.name_display == owner.name)
            if slots:
                slot = slots[0]
            else:
                layer = action.layers[0] if action.layers else action.layers.new("Pose")
                strip = layer.strips[0] if layer.strips else layer.strips.new(type="KEYFRAME")
                frame = template.action_frame_start if template else action.frame_range[0]
                slot = snapshot.create_slot(action, strip, frame=frame)
            track = animation.nla_tracks.get(name)
            if track is None:
                track = animation.nla_tracks.new()
                track.name = name
            clip = track.strips.new(action.name, 0, action)
            clip.action_slot = slot
            if template:
                clip.action_frame_start = template.action_frame_start
                clip.action_frame_end = template.action_frame_end
                clip.scale = template.scale
                clip.repeat = template.repeat
                clip.frame_start = template.frame_start
                clip.extrapolation = template.extrapolation
            clip.use_sync_length = True
        return bool(snapshots)
