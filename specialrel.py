#this is my special relativity project I will update it as I go along
#Packages
import matplotlib.pyplot as plt 
import numpy as np 


def lorentz_transformation(t,x,v):

    gamma = 1 / (np.sqrt(1-v**2))
    x_prime = gamma * (x - v*t)
    t_prime = gamma * (t - x*v )

    return x_prime, t_prime 


# Now, imagine a lamppost in some Frame S where it is stationary 


# Create a time array with 100 points
# This is the worldline of a stationary object at x=2 in Frame S
t1 = np.linspace(0, 10, 100)
x1 = np.full_like(t1, 2) # Creates an array of 2s, same size as t1
 
# Now, transform these coordinates to get the worldline in Frame S'
x_prime, t_prime = lorentz_transformation(t1, x1, 0.5)


fig, axs = plt.subplots(2, 1, figsize=(6, 8)) # 2 rows, 1 column

# Plot for Frame S
axs[0].plot(x1, t1)
axs[0].set_title('Frame S: Stationary Object')
axs[0].set_xlabel('Space (x)')
axs[0].set_ylabel('Time (ct)')
axs[0].set_xlim(-1, 10)
axs[0].set_ylim(-1, 11)
axs[0].grid(True)

# Plot for Frame S'
axs[1].plot(x_prime, t_prime)
axs[1].set_title("Frame S': Object appears to be moving")
axs[1].set_xlabel("Space (x')")
axs[1].set_ylabel("Time (ct')")
axs[1].set_xlim(-1, 10)
axs[1].set_ylim(-1, 11)
axs[1].grid(True)


plt.tight_layout()

plt.show()