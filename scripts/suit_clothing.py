"""Adapt the MPFB navy suit to the project's plain-shirt outfit."""
import bmesh


def remove_tie(obj):
    if obj.get('dance_wardrobe_asset') == 'toigo_male_suit_3' and not obj.get('dance_tie_removed'):
        # The original OBJ's independent tie island occupies vertices 390–1064.
        # Its shirt, jacket, buttons, and trousers use the remaining vertices.
        if len(obj.data.vertices) != 8527:
            raise ValueError('Use the original MPFB Suit3 mesh before removing its tie')
        mesh = bmesh.new()
        mesh.from_mesh(obj.data)
        mesh.verts.ensure_lookup_table()
        bmesh.ops.delete(mesh, geom=[mesh.verts[index] for index in range(390, 1065)], context='VERTS')
        mesh.to_mesh(obj.data)
        mesh.free()
        obj.data.update()
        obj['dance_tie_removed'] = True
