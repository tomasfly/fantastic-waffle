# test_data/newtons_laws_data.py

# Test data for Newton's Laws of Motion

# Constants
GRAVITY = 9.8  # Acceleration due to gravity in m/s^2
MASS = 10.0  # Mass of the object in kg
FORCE = 50.0  # Applied force on the object in N

# Variables
velocity = 0.0  # Initial velocity of the object in m/s
time = 5.0  # Time duration in seconds

# Expected results
expected_acceleration = FORCE / MASS  # Expected acceleration in m/s^2
expected_final_velocity = velocity + expected_acceleration * time  # Expected final velocity in m/s
expected_displacement = velocity * time + 0.5 * expected_acceleration * time**2  # Expected displacement in meters