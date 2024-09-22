import unittest
from law_of_large_numbers import calculate_mean, calculate_variance

class TestLawOfLargeNumbers(unittest.TestCase):
    def test_calculate_mean(self):
        # Test case 1: Positive numbers
        numbers = [1, 2, 3, 4, 5]
        expected_mean = 3.0
        self.assertEqual(calculate_mean(numbers), expected_mean)

        # Test case 2: Negative numbers
        numbers = [-1, -2, -3, -4, -5]
        expected_mean = -3.0
        self.assertEqual(calculate_mean(numbers), expected_mean)

        # Test case 3: Mixed positive and negative numbers
        numbers = [-1, 2, -3, 4, -5]
        expected_mean = -0.6
        self.assertAlmostEqual(calculate_mean(numbers), expected_mean)

    def test_calculate_variance(self):
        # Test case 1: Positive numbers
        numbers = [1, 2, 3, 4, 5]
        expected_variance = 2.5
        self.assertAlmostEqual(calculate_variance(numbers), expected_variance)

        # Test case 2: Negative numbers
        numbers = [-1, -2, -3, -4, -5]
        expected_variance = 2.5
        self.assertAlmostEqual(calculate_variance(numbers), expected_variance)

        # Test case 3: Mixed positive and negative numbers
        numbers = [-1, 2, -3, 4, -5]
        expected_variance = 7.04
        self.assertAlmostEqual(calculate_variance(numbers), expected_variance)

if __name__ == '__main__':
    unittest.main()