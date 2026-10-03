"""Evaluated skin clearance between separate body regions and participants."""

from itertools import combinations

from mathutils import Vector

from ergonomic_pose import BodySurface
from ergonomic_collisions import ArmBodyCollisions, SurfacePatch


class AnatomicalSurface(BodySurface):
    def __init__(self, context, rig):
        self.bone_regions = {}
        super().__init__(context, rig)

    def retrieve_region(self, bone):
        if bone not in self.bone_regions:
            self.bone_regions[bone] = self.retrieve_bone_region(bone)
        return self.bone_regions[bone]

    def retrieve_bone_region(self, bone):
        if bone.startswith(('DEF-f_', 'DEF-thumb')):
            return bone.removeprefix('DEF-')
        elif any(parent.name in {'ORG-spine.006', 'DEF-spine.006'}
                 for parent in self.rig.data.bones[bone].parent_recursive):
            return 'head'
        else:
            region = super().retrieve_region(bone)
            if region.startswith(('DEF-spine', 'DEF-pelvis', 'DEF-shoulder')):
                return 'torso'
            else:
                return region


class BodyClearance(ArmBodyCollisions):
    clearance = .0005

    def extend(self, surfaces):
        self.fitting = True
        try:
            super().extend(surfaces)
        finally:
            self.fitting = False

    def retrieve_candidates(self, source, target):
        candidates = super().retrieve_candidates(source, target)
        if getattr(self, 'fitting', False):
            direction = Vector(tuple(sum(source.bounds[axis]) - sum(target.bounds[axis]) for axis in range(3)))
            if direction.length > 1e-6:
                direction.normalize()
                # A crossing limb escapes through one side of a region. Opposing
                # surface planes would trap it inside the intersecting volume.
                candidates = [entry for entry in candidates if entry[4].dot(direction) > .1]
        return candidates

    def retrieve_patches(self, surface):
        regions = [surface.retrieve_region(bone) for bone in surface.bones]
        polygons = {}
        adjoining = set()
        for polygon in surface.polygons:
            members = {regions[index] for index in polygon}
            if len(members) == 1:
                polygons.setdefault(next(iter(members)), []).append(polygon)
            else:
                adjoining.update(frozenset(pair) for pair in combinations(members, 2))
        # Neighboring anatomical segments share deforming joint tissue.
        for name in set(surface.bones):
            bone = surface.rig.data.bones[name]
            if bone.parent and bone.parent.name.startswith('DEF-'):
                adjoining.add(frozenset((surface.retrieve_region(name), surface.retrieve_region(bone.parent.name))))
        for side in ('L', 'R'):
            for first, second in (('upper_arm', 'forearm'), ('forearm', 'hand'),
                                  ('thigh', 'knee'), ('knee', 'foot')):
                adjoining.add(frozenset((f'{first}.{side}', f'{second}.{side}')))
            for finger in ('f_index', 'f_middle', 'f_ring', 'f_pinky', 'thumb'):
                adjoining.add(frozenset((f'hand.{side}', f'{finger}.01.{side}')))
                for segment in (1, 2):
                    adjoining.add(frozenset((f'{finger}.{segment:02}.{side}', f'{finger}.{segment + 1:02}.{side}')))
        patches = [SurfacePatch(surface, region, faces) for region, faces in sorted(polygons.items())]
        for patch in patches:
            patch.bounds = [(min(surface.positions[index][axis] for index in patch.indices),
                             max(surface.positions[index][axis] for index in patch.indices)) for axis in range(3)]
        return patches, adjoining

    def retrieve_pairs(self, surfaces):
        groups = [self.retrieve_patches(surface) for surface in surfaces]
        pairs = []
        for index, (patches, adjoining) in enumerate(groups):
            pairs.extend((first, second) for first, second in combinations(patches, 2)
                         if frozenset((first.region, second.region)) not in adjoining)
            for other, _adjoining in groups[index + 1:]:
                pairs.extend((first, second) for first in patches for second in other)
        # Refreshing evaluated surfaces after each fit discovers newly approaching regions.
        return [(first, second) for first, second in pairs
                if all(first.bounds[axis][0] <= second.bounds[axis][1] + .005
                       and second.bounds[axis][0] <= first.bounds[axis][1] + .005 for axis in range(3))]
