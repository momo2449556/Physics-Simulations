#this is my special relativity project I will update it as I go along
#Packages
import matplotlib.pyplot as plt 
import numpy as np 


def lorentz_transformation(ct,x,v):

    gamma = 1 / (np.sqrt(1-v**2))
    x_prime = gamma * (x - v*ct)
    t_prime = gamma * (ct - x*v )

    return x_prime, t_prime 


#now imagine a lamppost in some Frame S where it is stationary 

#to create this already it becomes complicated what we need is a transformer (which we already have), a worldline generator, and finally a plotting machine showing the two frames.