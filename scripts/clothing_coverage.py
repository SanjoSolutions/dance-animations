"""Add body coverage for opaque, full-length garments with open cuffs."""
import bpy
from mathutils.bvhtree import BVHTree


def retrieve_rest_coordinates(body):
    coordinates = [vertex.co.copy() for vertex in body.data.vertices]
    if body.data.shape_keys:
        keys = body.data.shape_keys
        coordinates = [point.co.copy() for point in keys.reference_key.data]
        for key in keys.key_blocks:
            if key != keys.reference_key and key.value:
                for index, point in enumerate(key.data):
                    coordinates[index] += (point.co - key.relative_key.data[index].co) * key.value
    return coordinates


def separate_waist_layers(top, pants):
    transform = top.matrix_world.inverted() @ pants.matrix_world
    vertices = [transform @ vertex.co for vertex in pants.data.vertices]
    surface = BVHTree.FromPolygons(vertices, [tuple(polygon.vertices) for polygon in pants.data.polygons])
    waist = max(vertex.z for vertex in vertices)
    width = max(abs(vertex.x) for vertex in vertices)
    for vertex in top.data.vertices:
        if vertex.co.z < waist + .02 and abs(vertex.co.x) < width + .02:
            point, normal, index, distance = surface.find_nearest(vertex.co)
            if point is not None and distance < .04:
                separation = (vertex.co - point).dot(normal)
                if separation < .008:
                    vertex.co += normal * (.008 - separation)


def apply_full_length_coverage(body, garment):
    identifier = garment['dance_wardrobe_asset']
    if identifier in ('toigo_fisherman_sweater', 'toigo_wool_pants'):
        transform = body.matrix_world.inverted() @ garment.matrix_world
        coordinates = [transform @ vertex.co for vertex in garment.data.vertices]
        # Keep skin at the neckline, cuffs, and ankles inside the garment openings.
        lower = min(coordinate.z for coordinate in coordinates) + .012
        upper = max(coordinate.z for coordinate in coordinates) - .012
        width = max(abs(coordinate.x) for coordinate in coordinates) - .025
        hands = {group.index for group in body.vertex_groups
                 if group.name.startswith(('DEF-hand.', 'DEF-palm.', 'DEF-f_', 'DEF-thumb.'))}
        positions = retrieve_rest_coordinates(body)
        covered = [vertex.index for vertex, position in zip(body.data.vertices, positions)
                   if lower < position.z < upper and abs(position.x) < width
                   and sum(group.weight for group in vertex.groups if group.group in hands) < .5]
        name = 'Delete.' + identifier
        previous = body.vertex_groups.get(name)
        if previous:
            body.vertex_groups.remove(previous)
        group = body.vertex_groups.new(name=name)
        group.add(covered, 1, 'REPLACE')
        modifier = body.modifiers.get(name) or body.modifiers.new(name, 'MASK')
        modifier.vertex_group = group.name
        modifier.invert_vertex_group = True
