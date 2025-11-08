import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#This script uses Runge-Kutta 4 for time. 

# --- Simulation Parameters ---
N = 1000
L = 250
dx = L / N
v_speed = 1.0 
CFL = 0.7  # Courant-Friedrichs-Lewy condition (must be <= 1)
dt = CFL * dx / v_speed
total_steps = 3000

energy_kick = 0.001 # This bias allows the universe to set to +v 

# --- Potential Parameters ---
lambda_ = 1
v = 1.0
eta = 0.01 # Damping coefficient

# --- Grid and Initial Conditions ---
x = np.linspace(0, L, N)




noise_level = 0.01

random_bumps = np.random.rand(N) - 0.5

pi_now = (noise_level * random_bumps) 

phi_now = (noise_level * random_bumps) 

# --- Matplotlib Setup ---
fig, ax = plt.subplots()
ax.set_ylim(-v * 1.5, v * 1.5) 
ax.set_xlim(0, L)
ax.set_title("1D Phi-Four Model (Spontaneous Symmetry Breaking)")
ax.set_xlabel("Position (x)")
ax.set_ylabel("Field Value (φ)")
line, = ax.plot(x, phi_now, lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)



def laplacian(phi_n):

    laplacian = (np.roll(phi_n, -1) + np.roll(phi_n, 1) - 2 * phi_n) / dx**2

    return laplacian 

def v_prime(phi_n):

    v_prime = lambda_ * (np.power(phi_n, 3) - (v**2) * phi_n) 

    return v_prime 

def RK4(pi_n, phi_n, laplacian, potential):

    

    k1 = (pi_n, laplacian(phi_n) - potential(phi_n) - eta*pi_n )

    phi_shift1 = phi_n + dt/2 * k1[0]
    pi_shift1  = pi_n  + dt/2 * k1[1]

    k2 = (pi_shift1, laplacian(phi_shift1) - potential(phi_shift1) - eta * pi_shift1)

    phi_shift2  = phi_n + dt/2 * k2[0]
    pi_shift2 = pi_n + dt/2  * k2[1]

    k3 = (pi_shift2, laplacian(phi_shift2) - potential(phi_shift2) - eta * pi_shift2)

    phi_shift3  = phi_n + dt * k3[0]
    pi_shift3 = pi_n + dt  * k3[1]

    k4 = (pi_shift3, laplacian(phi_shift3) - potential(phi_shift3) - eta * pi_shift3)

    phi_next =  phi_n + dt /6 * (k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
    pi_next =  pi_n + dt /6 * (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])

    return phi_next, pi_next

    
def update(frame):
    global phi_now, pi_now
    
    # Compute next step using RK4
    phi_next, pi_next = RK4(pi_now, phi_now, laplacian, v_prime)
    
    # Update the state
    phi_now = phi_next
    pi_now  = pi_next

    # Update the plot
    line.set_ydata(phi_now)
    time_text.set_text(f"Time Step: {frame}")

    return line, time_text


ani = animation.FuncAnimation(
    fig, update, frames=total_steps, blit=True, interval=1, repeat=False
)

plt.grid(True)
plt.show()

print("Simulation finished.")
print(f"Parameters: N={N}, L={L}, dx={dx:.3f}, dt={dt:.3f}, CFL={CFL}")
print(f"Potential: lambda={lambda_}, v={v}, eta={eta}")