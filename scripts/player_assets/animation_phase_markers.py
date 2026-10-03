"""Carry a paired action's authored sections from Blender to Godot."""

MARKERS = ("entry_start", "activity_start", "activity_end", "dissolve_end")


class AnimationPhaseMarkers:
    def __init__(self, action):
        self.action = action

    def retrieve(self):
        values = {marker.name: marker.frame for marker in self.action.pose_markers}
        selected = {name: values[name] for name in MARKERS if name in values}
        if selected:
            if len(selected) != len(MARKERS):
                raise ValueError("Define entry_start, activity_start, activity_end, and dissolve_end together")
            frames = [selected[name] for name in MARKERS]
            if any(first >= second for first, second in zip(frames, frames[1:])):
                raise ValueError("Place paired animation markers in increasing frame order")
            start, end = self.action.frame_range
            if frames[0] < start or frames[-1] > end:
                raise ValueError("Keep paired animation markers inside the authored action range")
        return selected

    def store(self, entry_start, activity_start, activity_end, dissolve_end):
        frames = (entry_start, activity_start, activity_end, dissolve_end)
        if any(isinstance(frame, bool) or not isinstance(frame, int) for frame in frames):
            raise ValueError("Use whole frames for paired animation markers")
        if any(first >= second for first, second in zip(frames, frames[1:])):
            raise ValueError("Place paired animation markers in increasing frame order")
        for name, frame in zip(MARKERS, frames):
            marker = self.action.pose_markers.get(name) or self.action.pose_markers.new(name)
            marker.frame = frame
        return self.retrieve()

    def apply(self, clip, frame_rate):
        markers = self.retrieve()
        if markers:
            origin = self.action.frame_range[0]
            clip.setdefault("extras", {})["animation_markers"] = {
                name: (frame - origin) / frame_rate for name, frame in markers.items()
            }
        return bool(markers)
