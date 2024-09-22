# universal_gravitation.py

def calculate_gravitational_force(mass1, mass2, distance):
    """
    Calculates the gravitational force between two objects using Newton's Universal Law of Gravitation.

    Args:
        mass1 (float): Mass of the first object.
        mass2 (float): Mass of the second object.
        distance (float): Distance between the two objects.

    Returns:
        float: Gravitational force between the two objects.
    """
    gravitational_constant = 6.67430e-11
    force = (gravitational_constant * mass1 * mass2) / (distance ** 2)
    return force