"""Bind mesh shape-key editing to the animation selected in Helpers."""

from animation_participants import retrieve_active_action
from animation_viewport import AnimationViewport
from track_chooser import TrackChooser


class ShapeKeyAnimation:
    def synchronize(self, context, mesh):
        action = retrieve_active_action(context)
        keys = mesh.data.shape_keys
        if action and action.is_editable and keys.is_editable:
            chooser = TrackChooser(context.scene)
            name = chooser.retrieve_active_name() or action.name
            animation = keys.animation_data_create()
            slot = self.retrieve_slot(action, keys)
            AnimationViewport.suspended += 1
            try:
                if slot is None:
                    slot = action.slots.new("KEY", keys.name)
                if animation.action != action or animation.action_slot != slot:
                    if animation.action:
                        animation.action.use_fake_user = True
                    animation.use_tweak_mode = False
                    animation.action = action
                    animation.action_slot = slot
                if not animation.use_tweak_mode:
                    animation.use_nla = False
                    animation.action_blend_type = "REPLACE"
                    animation.action_influence = 1
                track = animation.nla_tracks.get(name)
                if track is None:
                    track = animation.nla_tracks.new()
                    track.name = name
                    track.mute = True
                if not any(strip.action == action and strip.action_slot == slot for strip in track.strips):
                    strip = track.strips.new(action.name, int(action.frame_range[0]), action)
                    strip.action_slot = slot
                    strip.use_sync_length = True
                action.use_fake_user = True
            finally:
                AnimationViewport.suspended -= 1

    @staticmethod
    def retrieve_slot(action, keys):
        animation = keys.animation_data
        if animation.action == action and animation.action_slot:
            return animation.action_slot
        matches = [strip.action_slot for track in animation.nla_tracks for strip in track.strips
                   if strip.action == action and strip.action_slot]
        if matches:
            return matches[0]
        return next((slot for slot in action.slots if slot.target_id_type == "KEY"
                     and (keys in slot.users() or (slot.identifier == "KE" + keys.name and not slot.users()))), None)
