import unittest
from src.universal_gravitation import calculate_gravitational_force

class UniversalGravitationTestCase(unittest.TestCase):
    def test_calculate_gravitational_force(self):
        # Test case 1: Calculate gravitational force between two objects
        mass1 = 10
        mass2 = 5
        distance = 2
        expected_force = 0.2
        calculated_force = calculate_gravitational_force(mass1, mass2, distance)
        self.assertAlmostEqual(calculated_force, expected_force, places=2)

        # Test case 2: Calculate gravitational force with different masses and distance
        mass1 = 20
        mass2 = 10
        distance = 5
        expected_force = 0.8
        calculated_force = calculate_gravitational_force(mass1, mass2, distance)
        self.assertAlmostEqual(calculated_force, expected_force, places=2)

        # Test case 3: Calculate gravitational force with zero mass
        mass1 = 0
        mass2 = 10
        distance = 2
        expected_force = 0
        calculated_force = calculate_gravitational_force(mass1, mass2, distance)
        self.assertAlmostEqual(calculated_force, expected_force, places=2)

if __name__ == '__main__':
    unittest.main()