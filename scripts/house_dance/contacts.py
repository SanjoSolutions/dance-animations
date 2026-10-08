"""Support heights from evaluated MPFB sole samples, in meters."""
import json
from pathlib import Path

from mathutils import Vector


class SoleContacts:
    def __init__(self):
        self.samples = json.loads(Path(__file__).with_name('soles.json').read_text())

    def retrieve_height(self, actor, side, rotation):
        return 0.001 - min((rotation @ Vector(point)).z
                           for point in self.samples[actor][side]['samples'])


class FloorSurface:
    def retrieve_nearest(self, point):
        return Vector((point.x, point.y, 0)), Vector((0, 0, 1))
