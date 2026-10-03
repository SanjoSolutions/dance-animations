"""Arm and breast surface separation for ergonomic pose fitting."""

from mathutils import Vector
from mathutils.bvhtree import BVHTree


class SurfacePatch:
    def __init__(self, surface, region, polygons):
        self.surface = surface
        self.region = region
        self.polygons = polygons
        self.indices = sorted({index for polygon in polygons for index in polygon})
        indices = {original: index for index, original in enumerate(self.indices)}
        self.tree = BVHTree.FromPolygons(
            [surface.positions[index] for index in self.indices],
            [tuple(indices[index] for index in polygon) for polygon in polygons])

    def retrieve_samples(self):
        samples = [(self.surface.positions[index], self.surface.bones[index]) for index in self.indices]
        if len(self.polygons) < 10000:
            samples.extend((sum((self.surface.positions[index] for index in polygon), Vector()) / len(polygon),
                            self.surface.bones[polygon[0]]) for polygon in self.polygons)
        return samples

    def retrieve_nearest(self, point):
        nearest, normal, polygon, distance = self.tree.find_nearest(point)
        vertex = min(self.polygons[polygon], key=lambda index: (self.surface.positions[index] - nearest).length)
        return nearest, normal, distance, self.surface.bones[vertex]


class SurfaceSeparation:
    def __init__(self, source, target, normal, clearance):
        self.source = source
        self.target = target
        self.normal = normal
        self.clearance = clearance

    def retrieve_residual(self):
        normal = self.target.retrieve_direction(self.normal)
        gap = (self.source.retrieve_position() - self.target.retrieve_position()).dot(normal)
        return min(0, gap - self.clearance) * 60


class ArmBodyCollisions:
    """Separate independently moving arm skin from each breast's surface patch."""

    clearance = .002
    tolerance = .0005

    def __init__(self, surfaces, reach):
        self.reach = reach
        self.separations = []
        self.extend(surfaces)

    @staticmethod
    def retrieve_patch_pairs(surface):
        arms = {f'{part}.{side}' for part in ('upper_arm', 'forearm', 'hand') for side in ('L', 'R')}
        breasts = {f'DEF-breast.{side}' for side in ('L', 'R')}
        regions = [surface.retrieve_region(bone) for bone in surface.bones]
        polygons = {region: [] for region in arms | breasts}
        for polygon in surface.polygons:
            region = regions[polygon[0]]
            if region in polygons and all(regions[index] == region for index in polygon):
                polygons[region].append(polygon)
        patches = {region: SurfacePatch(surface, region, faces) for region, faces in polygons.items() if faces}
        return [(patches[arm], patches[breast]) for arm in sorted(arms) for breast in sorted(breasts)
                if arm in patches and breast in patches]

    def retrieve_candidates(self, source, target):
        candidates = []
        for point, bone in source.retrieve_samples():
            nearest, normal, distance, target_bone = target.retrieve_nearest(point)
            gap = (point - nearest).dot(normal)
            # A negative distance at an open patch boundary describes its extended plane,
            # while a perpendicular projection describes penetration of the patch itself.
            interior = abs(gap) >= distance * .95
            if distance <= self.reach and (gap >= 0 or interior):
                candidates.append((gap, point, bone, nearest, normal, target_bone, interior))
        return candidates

    def extend(self, surfaces):
        from ergonomic_pose import SurfaceAnchor
        for first, second in self.retrieve_pairs(surfaces):
            for source, target in ((first, second), (second, first)):
                chosen = []
                for gap, point, bone, nearest, normal, target_bone, _interior in sorted(
                        self.retrieve_candidates(source, target), key=lambda item: item[0]):
                    if len(chosen) < 32 and all((point - previous).length > .012 for previous in chosen):
                        chosen.append(point)
                        self.separations.append(SurfaceSeparation(
                            SurfaceAnchor(source.surface.rig, bone, point),
                            SurfaceAnchor(target.surface.rig, target_bone, nearest), normal,
                            self.clearance if gap < 0 else min(self.clearance, gap)))

    def retrieve_pairs(self, surfaces):
        return [pair for surface in surfaces for pair in self.retrieve_patch_pairs(surface)]

    def retrieve_residual(self):
        return [separation.retrieve_residual() for separation in self.separations]

    def retrieve_overlaps(self, surfaces):
        overlaps = []
        for first, second in self.retrieve_pairs(surfaces):
            crossings = len(first.tree.overlap(second.tree))
            penetration = 0.0
            for source, target in ((first, second), (second, first)):
                for gap, _point, _bone, _nearest, _normal, _target_bone, interior in self.retrieve_candidates(source, target):
                    if interior:
                        penetration = max(penetration, -gap)
            if crossings or penetration > self.tolerance:
                overlaps.append({'rig': first.surface.rig.name, 'arm': first.region, 'body': second.region,
                                 'body_rig': second.surface.rig.name,
                                 'crossings': crossings, 'penetration': penetration})
        return overlaps
