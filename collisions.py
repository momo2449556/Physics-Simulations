from fourvectors import Matrix4x4, transform_vector, gamma_factor
from fourvectors import FourVector as four_vector
import numpy as np
import matplotlib.pyplot as plt 

# In this script I will show a charged Pion decay.
# Assuming natural units


neutrino_mass = 0 

muon_mass = 105.7

pion_mass = 139.6


initial_pion_momentum_lab = four_vector.from_mass_and_velocity(
    rest_mass=pion_mass,
    velocity_vector=[0.8, 0, 0]
)

# Velocities are for the easy Frame S' 

# 109.8 + 29.8 = 139.6 
pion_momentum = four_vector(109.8, 29.8, 0, 0)

neutrino_momentum = four_vector(29.8, -29.8, 0, 0)

lorentz = Matrix4x4.from_velocity(velocity_vector= [0.8, 0, 0])

S_muon = transform_vector(lorentz, pion_momentum)

S_neutrino = transform_vector(lorentz, neutrino_momentum)

if S_muon.data[0] + S_neutrino.data[0] == initial_pion_momentum_lab.data[0]:

    print("Simulation successful")

else:
    print (f"{S_muon.data[0] + S_neutrino.data[0]} compared to {initial_pion_momentum_lab.data[0]}")