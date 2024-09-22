# simple_harmonic_motion.py

def calculate_amplitude(mass, spring_constant):
    """
    Calculates the amplitude of a simple harmonic motion given the mass and spring constant.
    """
    amplitude = (mass * 9.8) / spring_constant
    return amplitude

def calculate_period(mass, spring_constant):
    """
    Calculates the period of a simple harmonic motion given the mass and spring constant.
    """
    period = 2 * 3.14159 * ((mass / spring_constant) ** 0.5)
    return period

def calculate_frequency(mass, spring_constant):
    """
    Calculates the frequency of a simple harmonic motion given the mass and spring constant.
    """
    frequency = 1 / calculate_period(mass, spring_constant)
    return frequency