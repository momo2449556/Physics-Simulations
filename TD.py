import matplotlib.pyplot as plt
import numpy as np

def lorentz_transformation(t,x,v):

    gamma = 1 / (np.sqrt(1-v**2))
    x_prime = gamma * (x - v*t)
    t_prime = gamma * (t - x*v )

    return x_prime, t_prime 

t1 = np.linspace(0, 10, 100)
x1 = np.full_like(t1, 2)
x2 = np.full_like(t1,4)

x_prime1, t_prime1 = lorentz_transformation(t1, x1, 0.5)
x_prime2, t_prime2 = lorentz_transformation(t1,x2, 0.5)


fig, axs = plt.subplots(2, 1, figsize=(6, 8)) 

axs[0].plot(x1, t1)
axs[0].set_title('Frame S: Stationary Object')
axs[0].set_xlabel('Space (x)')
axs[0].set_ylabel('Time (ct)')
axs[0].set_xlim(-1, 10)
axs[0].set_ylim(-1, 11)
axs[0].grid(True)

axs[1].plot(x_prime1, t_prime1)
axs[1].set_title("Frame S'")
axs[1].set_xlabel("Space (x')")
axs[1].set_ylabel("Time (ct')")
axs[1].set_xlim(-1, 10)
axs[1].set_ylim(-1, 11)
axs[1].grid(True)

plt.tight_layout()

plt.show()


def calculate_interval(event1, event2):
    t1, x1 = event1
    t2, x2 = event2
    dt = t1 - t2
    dx = x1 - x2
    interval_squared = dt**2 - dx**2
    return interval_squared

event_A_in_S = (t1[0], x1[0])
event_B_in_S = (t1[-1], x1[-1])

event_A_in_S_prime = (t_prime1[0], x_prime1[0])
event_B_in_S_prime = (t_prime1[-1], x_prime1[-1])

interval_S = calculate_interval(event_A_in_S, event_B_in_S)
interval_S_prime = calculate_interval(event_A_in_S_prime, event_B_in_S_prime)

print("\n--- Spacetime Interval Calculation ---")
print(f"Interval in Frame S: {interval_S:.2f}")
print(f"Interval in Frame S': {interval_S_prime:.2f}")

# The time elapsed in the clock's own rest frame (S) is the proper time.
proper_time = t1[-1] - t1[0]

# The time measured by the observer who sees the clock moving (S') is the dilated time.
dilated_time1 = t_prime1[-1] - t_prime1[0]
dilated_time2 = t_prime2[-1] - t_prime2[0]

print(f"Time on clock at rest (Proper Time): {proper_time:.2f}")
print(f"Time measured by moving observer (Dilated Time): {dilated_time1:.2f}")

print(f"Time measured by moving observer (Dilated Time): {dilated_time2:.2f}")