"""Shared vertical contact forces and moments for a group of posed bodies."""

import numpy as np


class SupportEquilibrium:
    """Fit compressive forces, including equal/opposite participant contact loads."""

    def retrieve_residual(self, centers, masses, contacts):
        # Each contact is (supported participant, supporting participant or None, point).
        matrix = np.zeros((3 * len(centers), len(contacts)))
        desired = np.zeros(3 * len(centers))
        desired[::3] = masses
        for column, (supported, supporting, point) in enumerate(contacts):
            for participant, direction in ((supported, 1), (supporting, -1)):
                if participant is not None:
                    offset = np.asarray(point)[:2] - centers[participant][:2]
                    matrix[participant * 3:participant * 3 + 3, column] = (
                        direction, direction * offset[0], direction * offset[1])
        forces = self.retrieve_compressive_forces(matrix, desired)
        return matrix @ forces - desired

    @staticmethod
    def retrieve_compressive_forces(matrix, desired):
        """Small active-set nonnegative least squares using Blender's bundled NumPy."""
        forces = np.zeros(matrix.shape[1])
        active = np.zeros(matrix.shape[1], dtype=bool)
        for _iteration in range(max(1, matrix.shape[1] * 3)):
            gradient = matrix.T @ (desired - matrix @ forces)
            available = np.where(~active, gradient, -np.inf)
            if available.size and np.max(available) > 1e-9:
                active[np.argmax(available)] = True
                for _step in range(matrix.shape[1] + 1):
                    trial = np.zeros_like(forces)
                    trial[active] = np.linalg.lstsq(matrix[:, active], desired, rcond=1e-8)[0]
                    if np.all(trial[active] > 0):
                        forces = trial
                        break
                    crossing = active & (trial <= 0)
                    denominator = forces[crossing] - trial[crossing]
                    ratios = np.divide(forces[crossing], denominator,
                                       out=np.zeros_like(denominator), where=denominator > 0)
                    forces += np.min(ratios) * (trial - forces)
                    active[forces <= 1e-10] = False
            else:
                break
        return forces
