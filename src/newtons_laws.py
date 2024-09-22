import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.81  # gravity (m/s^2)
v0 = 20  # initial velocity (m/s)
theta = np.radians(45)  # launch angle (degrees converted to radians)

# Velocity components
v0x = v0 * np.cos(theta)
v0y = v0 * np.sin(theta)

# Flight time
t_total = 2 * v0y / g

# Time intervals
t = np.linspace(0, t_total, num=500)

# Trajectory
x = v0x * t
y = v0y * t - 0.5 * g * t**2

# Plot
plt.plot(x, y)
plt.title('Projectile Motion')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.show()

def gravitational_force(m1, m2, r):
    G = 6.67430e-11  # gravitational constant in N·m²/kg²
    return G * (m1 * m2) / (r**2)

m1 = 5.97e24  # mass of the Earth in kg
m2 = 7.35e22  # mass of the Moon in kg
r = 3.844e8   # distance between Earth and Moon in meters

F = gravitational_force(m1, m2, r)
print(f"Gravitational force between Earth and Moon: {F:.2e} N")

# Parameters
A = 1  # amplitude
omega = 2 * np.pi  # angular frequency (rad/s)
phi = 0  # initial phase
t = np.linspace(0, 10, num=500)  # time

# Position as a function of time
x = A * np.cos(omega * t + phi)

# Plot
plt.plot(t, x)
plt.title('Simple Harmonic Motion')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.show()
