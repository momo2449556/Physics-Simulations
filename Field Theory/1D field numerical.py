import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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


pi_now = noise_level * (random_bumps) 

phi_now = (noise_level * random_bumps) 

phi_prev = phi_now - pi_now * dt

# --- Matplotlib Setup ---
fig, ax = plt.subplots()
ax.set_ylim(-v * 1.5, v * 1.5) 
ax.set_xlim(0, L)
ax.set_title("1D Phi-Four Model (Spontaneous Symmetry Breaking)")
ax.set_xlabel("Position (x)")
ax.set_ylabel("Field Value (φ)")
line, = ax.plot(x, phi_now, lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

# --- Animation/Update Function ---
def update(frame):
    """
    Performs one time step of the simulation.
    """
    global phi_now, phi_prev, phi_next

    if frame < 250:

        laplacian = np.roll(phi_now, -1) + np.roll(phi_now, 1) - 2 * phi_now
    
        V_prime = lambda_ * (np.power(phi_now, 3) - (v**2) * phi_now) 

        damping_factor = eta * dt
    
        phi_next = 2 * phi_now - phi_prev \
                   + (CFL**2) * laplacian \
                   - (dt**2) * V_prime \
                 - damping_factor * (phi_now - phi_prev)  # Non Linear damping term added

        phi_prev = phi_now.copy()
        phi_now = phi_next.copy()

        line.set_ydata(phi_now)
        time_text.set_text(f"Time Step: {frame}")
    # Only add in energy kick after 250 frames
    else:

        laplacian = np.roll(phi_now, -1) + np.roll(phi_now, 1) - 2 * phi_now
    
        V_prime = lambda_ * (np.power(phi_now, 3) - (v**2) * phi_now) - energy_kick

        damping_factor = eta * dt 
    
        phi_next = 2 * phi_now - phi_prev \
                   + (CFL**2) * laplacian \
                   - (dt**2) * V_prime \
                - damping_factor * (phi_now - phi_prev)

        phi_prev = phi_now.copy()
        phi_now = phi_next.copy()

        line.set_ydata(phi_now)
        time_text.set_text(f"Time Step: {frame}")
    
    return line, time_text

# --- Run the Animation ---
ani = animation.FuncAnimation(
    fig, update, frames=total_steps, blit=True, interval=1, repeat=False
)

plt.grid(True)
plt.show()

print("Simulation finished.")
print(f"Parameters: N={N}, L={L}, dx={dx:.3f}, dt={dt:.3f}, CFL={CFL}")
print(f"Potential: lambda={lambda_}, v={v}, eta={eta}")
