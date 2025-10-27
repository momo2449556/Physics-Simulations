import numpy as np

def lorentz_transformation(t,x,v):

    gamma = 1 / (np.sqrt(1-v**2))
    x_prime = gamma * (x - v*t)
    t_prime = gamma * (t - x*v )

    return x_prime, t_prime 

def calculate_interval(event1, event2):
    t1, x1 = event1
    t2, x2 = event2
    dt = t1 - t2
    dx = x1 - x2
    interval_squared = dt**2 - dx**2
    return interval_squared


def length_contraction(x1,x2):

    return x1 - x2 

def time_dilation(t1,t2):

    return t2 - t1