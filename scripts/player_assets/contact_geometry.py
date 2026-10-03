"""Godot entrance-footprint measurement for evaluated Blender triangle meshes."""

from dataclasses import dataclass, field
from math import cos, pi, sin, sqrt

import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree
from mathutils.geometry import convex_hull_2d


TOLERANCE = 1e-7


@dataclass
class ContactMeasurement:
    intersecting: bool = False
    footprint: list = field(default_factory=list)

    def include(self, other):
        self.intersecting |= other.intersecting
        self.footprint.extend(other.footprint)

    def retrieve_diameter(self):
        points = self.footprint
        hull = convex_hull_2d(points) if len(points) > 2 else range(len(points))
        return sqrt(max(((points[a] - points[b]).length_squared
                         for a in hull for b in hull), default=0.0))


class ReceivingCylinder:
    """A convex, inscribed cylinder along local Y; dimensions use scene units."""

    def __init__(self, transform, diameter, height, resolution=12):
        radius = diameter / 2
        self.vertices = [transform @ Vector((radius * cos(2*pi*i/resolution), y,
                                            radius * sin(2*pi*i/resolution)))
                         for y in (-height/2, height/2) for i in range(resolution)]
        self.faces = [list(range(resolution)), list(range(resolution, 2*resolution))]
        self.faces.extend([[i, (i+1) % resolution, (i+1) % resolution + resolution,
                            i + resolution] for i in range(resolution)])
        normals = [Vector((0, -1, 0)), Vector((0, 1, 0))]
        normals.extend(Vector((cos(2*pi*(i+0.5)/resolution), 0,
                               sin(2*pi*(i+0.5)/resolution))) for i in range(resolution))
        normal_matrix = transform.to_3x3().inverted().transposed()
        self.planes = []
        for face, normal in zip(self.faces, normals):
            normal = (normal_matrix @ normal).normalized()
            self.planes.append((normal, normal.dot(self.vertices[face[0]])))
        coordinates = np.array(self.vertices)
        self.minimum, self.maximum = coordinates.min(axis=0), coordinates.max(axis=0)
        self.origin = transform.translation.copy()

    def contains(self, point):
        return all(normal.dot(point) - offset <= TOLERANCE for normal, offset in self.planes)

    def overlaps_bounds(self, coordinates):
        coordinates = np.asarray(coordinates)
        return bool(len(coordinates) and np.all(coordinates.max(axis=0) >= self.minimum)
                    and np.all(coordinates.min(axis=0) <= self.maximum))


class ContactMesh:
    """A snapshot of a closed mesh, including its modifiers and world transform."""

    def __init__(self, vertices, triangles):
        self.vertices = np.asarray(vertices, dtype=float).reshape((-1, 3))
        self.indices = np.asarray(triangles, dtype=int).reshape((-1, 3))
        self.triangles = self.vertices[self.indices]
        self.tree = None

    def matches(self, other):
        return (np.array_equal(self.vertices, other.vertices)
                and np.array_equal(self.indices, other.indices))

    @classmethod
    def from_object(cls, obj, graph):
        evaluated = obj.evaluated_get(graph)
        mesh = evaluated.to_mesh()
        try:
            mesh.calc_loop_triangles()
            vertices = np.empty(len(mesh.vertices)*3, dtype=float)
            mesh.vertices.foreach_get('co', vertices)
            triangles = np.empty(len(mesh.loop_triangles)*3, dtype=int)
            mesh.loop_triangles.foreach_get('vertices', triangles)
            transform = np.array(evaluated.matrix_world)
            vertices = vertices.reshape((-1, 3)) @ transform[:3, :3].T + transform[:3, 3]
            return cls(vertices, triangles)
        finally:
            evaluated.to_mesh_clear()

    def contains(self, point):
        if self.tree is None:
            self.tree = BVHTree.FromPolygons(self.vertices.tolist(), self.indices.tolist(), all_triangles=True)
        # Parity supports concave surfaces and either triangle winding.
        direction = Vector((0.8731, 0.3713, 0.3167)).normalized()
        origin = point.copy()
        crossings = 0
        while True:
            location, normal, index, distance = self.tree.ray_cast(origin, direction)
            if location is None:
                break
            crossings += 1
            origin = location + direction * TOLERANCE * 4
        return crossings % 2 == 1


    @classmethod
    def shaft_from_bone(cls, armature, bone_name, graph, radius=0.025, segments=12):
        """Build a closed cylinder along a posed armature bone for anatomy contact."""
        evaluated = armature.evaluated_get(graph)
        if bone_name not in evaluated.pose.bones:
            return cls(np.zeros((0, 3)), np.zeros((0, 3), dtype=int))
        bone = evaluated.pose.bones[bone_name]
        length = max(evaluated.data.bones[bone_name].length, 1e-4)
        matrix = evaluated.matrix_world @ bone.matrix
        rings = []
        for y in (0.0, length):
            for i in range(segments):
                angle = 2 * pi * i / segments
                rings.append(matrix @ Vector((radius * cos(angle), y, radius * sin(angle))))
        vertices = np.asarray([[point.x, point.y, point.z] for point in rings], dtype=float)
        triangles = []
        # Cap at bone head
        for k in range(1, segments - 1):
            triangles.append([0, k, k + 1])
        # Cap at bone tip (reversed winding)
        base = segments
        for k in range(1, segments - 1):
            triangles.append([base, base + k + 1, base + k])
        # Side quads as triangles
        for i in range(segments):
            j = (i + 1) % segments
            triangles.append([i, j, segments + j])
            triangles.append([i, segments + j, segments + i])
        return cls(vertices, triangles)


    @classmethod
    def shafts_from_bones(cls, armature, bone_names, graph, radius=0.012, segments=10):
        """Merge closed cylinders along posed bones for hand/finger contact."""
        vertices = []
        triangles = []
        for bone_name in bone_names:
            shaft = cls.shaft_from_bone(armature, bone_name, graph, radius=radius, segments=segments)
            if len(shaft.vertices) == 0:
                continue
            offset = len(vertices)
            vertices.extend(shaft.vertices.tolist())
            triangles.extend((shaft.indices + offset).tolist())
        if not vertices:
            return cls(np.zeros((0, 3)), np.zeros((0, 3), dtype=int))
        return cls(vertices, triangles)

class EntryIntersection:
    """Clip receiving surfaces against entering meshes, then project the entrance."""

    @staticmethod
    def _clip(points, planes):
        for normal, offset in planes:
            if len(points) == 2:
                first, second = [normal.dot(point) - offset for point in points]
                if first > TOLERANCE and second > TOLERANCE:
                    points = []
                elif first * second < 0:
                    crossing = points[0].lerp(points[1], first / (first - second))
                    points[0 if first > 0 else 1] = crossing
            elif len(points) >= 3:
                clipped = []
                for index, point in enumerate(points):
                    previous = points[index-1]
                    first, second = normal.dot(previous)-offset, normal.dot(point)-offset
                    if (first > TOLERANCE) != (second > TOLERANCE):
                        clipped.append(previous.lerp(point, first / (first-second)))
                    if second <= TOLERANCE:
                        clipped.append(point)
                points = clipped
        return points

    def measure(self, receiver, mesh, direction):
        result = ContactMeasurement()
        if len(mesh.triangles) and direction.length_squared > TOLERANCE and receiver.overlaps_bounds(mesh.vertices):
            axis = direction.normalized()
            reference = Vector((0, 1, 0)) if abs(axis.y) < 0.9 else Vector((1, 0, 0))
            horizontal = axis.cross(reference).normalized()
            vertical = axis.cross(horizontal)
            contained = {}
            triangles = mesh.triangles[
                np.all(mesh.triangles.max(axis=1) >= receiver.minimum-TOLERANCE, axis=1)
                & np.all(mesh.triangles.min(axis=1) <= receiver.maximum+TOLERANCE, axis=1)]
            for face, (normal, offset) in zip(receiver.faces, receiver.planes):
                entrance = normal.dot(axis) < -1e-6
                distances = triangles @ np.array(normal) - offset
                crossing = np.flatnonzero((distances.min(axis=1) <= TOLERANCE)
                                          & (distances.max(axis=1) >= -TOLERANCE))
                points = []
                for index in crossing:
                    triangle, values = triangles[index], distances[index]
                    section = [Vector(triangle[i]) for i in range(3) if abs(values[i]) <= TOLERANCE]
                    for first, second in ((0, 1), (1, 2), (2, 0)):
                        if values[first] * values[second] < 0 and min(abs(values[first]), abs(values[second])) > TOLERANCE:
                            section.append(Vector(triangle[first] + (triangle[second]-triangle[first])
                                                  * values[first]/(values[first]-values[second])))
                    clipped = self._clip(section, receiver.planes)
                    if len(clipped) >= 2:
                        result.intersecting = True
                        points.extend(clipped)
                for index in face:
                    if index not in contained:
                        contained[index] = mesh.contains(receiver.vertices[index])
                    if contained[index]:
                        result.intersecting = True
                        points.append(receiver.vertices[index])
                if entrance:
                    result.footprint.extend(Vector(((point-receiver.origin).dot(horizontal),
                                                    (point-receiver.origin).dot(vertical))) for point in points)
            if not result.intersecting:
                result.intersecting = any(receiver.contains(Vector(point)) for point in mesh.vertices)
        return result
