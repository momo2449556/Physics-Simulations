# The purpose of this script is to provide a toolkit for special relativity calculations
# using four-vector notation.
# This entire script assumes natural units where c = 1.

import numpy as np

def gamma_factor(v_squared):
    """
    Calculates the Lorentz gamma factor from the velocity-squared.
    Assumes c=1.
    """
    if v_squared >= 1:
        raise ValueError("Velocity-squared cannot be >= 1")
    return 1 / np.sqrt(1 - v_squared)


class FourVector:
    """A class to represent a 4-vector for special relativity."""
    def __init__(self, c0, c1, c2, c3):
        self.data = np.array([c0, c1, c2, c3], dtype=float)

    def __repr__(self):
        """Provides a clean string representation for printing."""
        return f"FourVector({self.data[0]:.2f}, {self.data[1]:.2f}, {self.data[2]:.2f}, {self.data[3]:.2f})"
    
    def calculate_interval_squared(self):
        """Calculates the invariant s^2 = (c0)^2 - (c1)^2 - (c2)^2 - (c3)^2."""
        sum_of_spatial_squares = np.sum(self.data[1:]**2)
        return self.data[0]**2 - sum_of_spatial_squares

    @classmethod
    def from_mass_and_velocity(cls, rest_mass, velocity_vector):
        """Creates a four-momentum vector from a particle's rest mass and 3D velocity."""
        vx, vy, vz = velocity_vector
        v_squared = vx**2 + vy**2 + vz**2
        
        gamma = gamma_factor(v_squared)
        
        energy = gamma * rest_mass
        px = gamma * rest_mass * vx
        py = gamma * rest_mass * vy
        pz = gamma * rest_mass * vz
        
        return cls(energy, px, py, pz)


class Matrix4x4:
    """A class to represent a 4x4 transformation matrix."""
    def __init__(self, matrix_data):
        self.data = np.asarray(matrix_data, dtype=float)

    def __repr__(self):
        # Using np.round to make the printed matrix cleaner
        return str(np.round(self.data, 2))

    @classmethod
    def from_velocity(cls, velocity_vector):
        """Creates a Lorentz boost matrix from a 3D velocity vector."""
        vx, vy, vz = velocity_vector
        v_squared = vx**2 + vy**2 + vz**2

        if v_squared == 0:
            return cls(np.identity(4))
        
        g = gamma_factor(v_squared)

        matrix_data = np.array([
            [g, -g * vx, -g * vy, -g * vz],
            [-g * vx, 1 + (g - 1) * vx**2 / v_squared, (g - 1) * vx * vy / v_squared, (g - 1) * vx * vz / v_squared],
            [-g * vy, (g - 1) * vy * vx / v_squared, 1 + (g - 1) * vy**2 / v_squared, (g - 1) * vy * vz / v_squared],
            [-g * vz, (g - 1) * vz * vx / v_squared, (g - 1) * vz * vy / v_squared, 1 + (g - 1) * vz**2 / v_squared]
        ])
        
        return cls(matrix_data)


def transform_vector(lorentz_matrix, initial_vector):
    """
    Performs the Lorentz transformation using matrix multiplication.
    Returns a new, transformed FourVector object.
    """
    transformed_data = lorentz_matrix.data @ initial_vector.data
    return FourVector(*transformed_data)
