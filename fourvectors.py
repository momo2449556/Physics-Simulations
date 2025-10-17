# The purpose of this script is to do the previous scripts in 4 vector notation, and expand it to more dimensions. To do this I will utilise classes.
# This entire script will make c = 1

import numpy as np 
import matplotlib.pyplot as plt

# Assumes an input of v_squared
def gamma_factor(v):
    g = 1 / np.sqrt(1 - v)

class four_vector:
    def __init__(self, t, x, y, z):

        self.data = np.array([t, x, y, z])

    def __repr__(self):
        
        return f"(t = {self.data[0]}, x = {self.data[1]}, y = {self.data[2]}, z = {self.data[3]})"
    
    def calculate_interval(self):

        sum = 0
        for i in range(1, 4):

            sum += self.data[i] **2

        s_squared = self.data[0] ** 2 - sum

        return s_squared
    

class Matrix4x4:
    def __init__(self, matrix_data):
        
        self.data = np.asarray(matrix_data)

    def __repr__(self):
        
        return str(self.data)

    @classmethod
    def from_velocity(cls, velocity_vector):
        
        vx, vy, vz = velocity_vector
        v_squared = vx**2 + vy**2 + vz**2

        # Handle the edge case of zero velocity
        if v_squared == 0:
            return cls(np.identity(4))

        
        gamma = gamma_factor(v_squared)

        matrix_data = np.array([
            [gamma, -gamma * vx, -gamma * vy, -gamma * vz],
            [-gamma * vx, 1 + (gamma - 1) * vx**2 / v_squared, (gamma - 1) * vx * vy / v_squared, (gamma - 1) * vx * vz / v_squared],
            [-gamma * vy, (gamma - 1) * vy * vx / v_squared, 1 + (gamma - 1) * vy**2 / v_squared, (gamma - 1) * vy * vz / v_squared],
            [-gamma * vz, (gamma - 1) * vz * vx / v_squared, (gamma - 1) * vz * vy / v_squared, 1 + (gamma - 1) * vz**2 / v_squared]
        ])
        
       
        return cls(matrix_data)


def transformation(lorentz_matrix, initial_vector):
    
    matrix_data = lorentz_matrix.data
    vector_data = initial_vector.data

    # Perform the matrix multiplication
    transformed_data = matrix_data @ vector_data

    t_prime, x_prime, y_prime, z_prime = transformed_data

    return four_vector(t_prime, x_prime, y_prime, z_prime)

#class Particle: