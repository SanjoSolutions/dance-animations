"""Match object and shape key actions to the saved baked rig clips."""


class AnimationExportTracks:
    def __init__(self, rigs):
        self.rigs = set(rigs)
        self.names = {
            strip.action.name
            for rig in rigs if rig.animation_data
            for track in rig.animation_data.nla_tracks
            for strip in track.strips
            if strip.action and strip.action.name.endswith((".baked", "_baked"))
        }

    def retrieve_name(self, name):
        matches = self.names.intersection({name, name + ".baked", name + "_baked"})
        if len(matches) > 1:
            raise RuntimeError(f"Use the full baked clip name for {name}")
        return next(iter(matches), None)

    def includes(self, owner):
        animation = owner.animation_data
        return bool(animation and (
            (animation.action and self.retrieve_name(animation.action.name))
            or any(self.retrieve_track_name(track) for track in animation.nla_tracks)
        ))

    def prepare(self, owner):
        animation = owner.animation_data
        if animation:
            # Exit strip editing before changing tracks or the active action.
            if animation.use_tweak_mode:
                animation.use_tweak_mode = False
            selected = [
                (track, self._retrieve_rig_track_name(track) if owner in self.rigs else self.retrieve_track_name(track))
                for track in animation.nla_tracks
            ]
            active_action = animation.action
            active_slot = animation.action_slot
            active_name = self.retrieve_name(active_action.name) if active_action and owner not in self.rigs else None
            names = [name for track, name in selected if name]
            if len(names) != len(set(names)):
                raise RuntimeError(f"Use one NLA track per baked clip on {owner.name}")
            for track, name in selected:
                if name:
                    track.name = "ExportTrack"
                    track.mute = False
                    track.is_solo = False
                else:
                    animation.nla_tracks.remove(track)
            for track, name in selected:
                if name:
                    track.name = name
            animation.action = None
            if active_name and all(name != active_name for track, name in selected):
                track = animation.nla_tracks.new()
                track.name = active_name
                strip = track.strips.new(active_action.name, int(active_action.frame_range[0]), active_action)
                strip.action_slot = active_slot
                # Copied owners can initially select an empty slot. Apply the
                # authored range after assigning the slot that holds the curves.
                strip.action_frame_start, strip.action_frame_end = active_action.frame_range
            animation.use_nla = True

    def _retrieve_rig_track_name(self, track):
        names = {strip.action.name if strip.action else None for strip in track.strips}
        if names and names <= self.names and len(names) > 1:
            raise RuntimeError(f"Place each baked clip on its own NLA track: {track.name}")
        return names.pop() if len(names) == 1 and names <= self.names else None

    def retrieve_track_name(self, track):
        actions = [strip.action for strip in track.strips if strip.action]
        name = self.retrieve_name(track.name)
        if actions and name is None:
            names = {self.retrieve_name(action.name) for action in actions}
            if len(names) == 1:
                name = names.pop()
        return name if actions else None


def retrieve_animation_owners(obj):
    owners = [obj]
    if obj.type == "MESH" and obj.data.shape_keys:
        owners.append(obj.data.shape_keys)
    return owners
