# Test data for Simple Harmonic Motion

amplitude = 2.5  # Amplitude of the motion
frequency = 1.8  # Frequency of the motion
phase = 0.5  # Phase of the motion
time = 3.2  # Time at which to calculate the position

expected_position = amplitude * math.cos(2 * math.pi * frequency * time + phase)  # Expected position at the given time