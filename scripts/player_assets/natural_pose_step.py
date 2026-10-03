"""Damped correction steps within the available control movement bounds."""

import numpy as np


class PoseStep:
    def __init__(self, jacobian, residual, bounds, values=None, damping=.0009):
        values = np.zeros(len(bounds)) if values is None else values
        self.lower = np.maximum(-.2, -bounds - values)
        self.upper = np.minimum(.2, bounds - values)
        self.curvature = jacobian.T @ jacobian + np.eye(len(bounds)) * damping
        self.gradient = jacobian.T @ residual

    def retrieve(self):
        step = np.linalg.solve(self.curvature, -self.gradient)
        if np.all(step >= self.lower) and np.all(step <= self.upper):
            return step
        else:
            # Coordinate minimization keeps each bounded update descending, even
            # when clipping an unconstrained coupled solution would increase error.
            step = np.zeros(len(self.gradient))
            gradient = self.gradient.copy()
            for _iteration in range(128):
                largest = 0.
                for index in range(len(step)):
                    value = np.clip(step[index] - gradient[index] / self.curvature[index, index],
                                    self.lower[index], self.upper[index])
                    change = value - step[index]
                    step[index] = value
                    gradient += self.curvature[:, index] * change
                    largest = max(largest, abs(change))
                if largest < 1e-7:
                    break
            return step
