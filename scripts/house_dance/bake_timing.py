"""Sample the native bakery at half frames while retaining editable 24 fps sources."""
import bpy


class BakeTiming:
    def __init__(self, action):
        self.action = action
        self.scene = bpy.context.scene
        self.rate = self.scene.render.fps
        self.base = self.scene.render.fps_base
        self.frame = self.scene.frame_current_final

    def retime(self, factor):
        family = {action for action in bpy.data.actions if action.name in
                  (self.action.name, self.action.name + '.baked')}
        for action in family:
            start, end = action.frame_range
            for layer in action.layers:
                for strip in layer.strips:
                    for bag in strip.channelbags:
                        for curve in bag.fcurves:
                            for point in curve.keyframe_points:
                                time, left, right = point.co.x, point.handle_left.x, point.handle_right.x
                                point.co.x = time * factor
                                point.handle_left.x = left * factor
                                point.handle_right.x = right * factor
                            curve.update()
            action.use_frame_range = True
            action.frame_start, action.frame_end = start * factor, end * factor
        for owner in self.scene.objects:
            if owner.animation_data:
                for track in owner.animation_data.nla_tracks:
                    for strip in track.strips:
                        if strip.action in family:
                            strip.use_sync_length = False
                            strip.action_frame_start, strip.action_frame_end = strip.action.frame_range
                            strip.frame_start, strip.frame_end = strip.action.frame_range
                            strip.use_sync_length = True

    def __enter__(self):
        self.retime(2)
        self.scene.render.fps = self.rate * 2
        return self

    def __exit__(self, *_error):
        self.retime(.5)
        self.scene.render.fps, self.scene.render.fps_base = self.rate, self.base
        self.scene.frame_set(int(self.frame), subframe=self.frame % 1)
