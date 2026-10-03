"""Evaluate skin anchors in batches using each bone's current world frame."""

import numpy as np


class PoseSurfaceSamples:
    def __init__(self, samples, separations):
        self.sample_count = len(samples)
        self.frames = []
        frame_indices = {}
        anchors = list(samples) + [entry.source for entry in separations] + [entry.target for entry in separations]
        indices = []
        for anchor in anchors:
            key = (anchor.rig.name, anchor.bone)
            if key not in frame_indices:
                frame_indices[key] = len(self.frames)
                self.frames.append((anchor.rig, anchor.rig.pose.bones[anchor.bone]))
            indices.append(frame_indices[key])
        self.indices = np.array(indices, dtype=int)
        self.positions = np.array([(*anchor.local, 1) for anchor in anchors]).reshape((-1, 4))
        self.directions = np.array([entry.target.orientation @ entry.normal for entry in separations]).reshape((-1, 3))
        self.clearances = np.array([entry.clearance for entry in separations])

    def retrieve(self):
        frames = [rig.matrix_world @ bone.matrix for rig, bone in self.frames]
        matrices = np.array(frames).reshape((-1, 4, 4))
        positions = np.einsum('nij,nj->ni', matrices[self.indices, :3, :], self.positions)
        count = len(self.clearances)
        if count:
            rotations = np.array([frame.to_quaternion().to_matrix() for frame in frames])
            normals = np.einsum('nij,nj->ni', rotations[self.indices[-count:]], self.directions)
            gaps = np.einsum('ni,ni->n', positions[self.sample_count:self.sample_count + count] - positions[-count:], normals)
            collisions = np.minimum(0, gaps - self.clearances) * 60
        else:
            collisions = np.empty(0)
        return positions[:self.sample_count], collisions
