import unittest
from src.fibonacci_sequence import generate_fibonacci_sequence

class TestFibonacciSequence(unittest.TestCase):
    def test_generate_fibonacci_sequence(self):
        # Test case 1: Check the first 10 numbers in the Fibonacci sequence
        expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        actual_sequence = generate_fibonacci_sequence(10)
        self.assertEqual(actual_sequence, expected_sequence)

        # Test case 2: Check the first 5 numbers in the Fibonacci sequence
        expected_sequence = [0, 1, 1, 2, 3]
        actual_sequence = generate_fibonacci_sequence(5)
        self.assertEqual(actual_sequence, expected_sequence)

        # Test case 3: Check the first 1 number in the Fibonacci sequence
        expected_sequence = [0]
        actual_sequence = generate_fibonacci_sequence(1)
        self.assertEqual(actual_sequence, expected_sequence)

        # Test case 4: Check an empty sequence
        expected_sequence = []
        actual_sequence = generate_fibonacci_sequence(0)
        self.assertEqual(actual_sequence, expected_sequence)

if __name__ == '__main__':
    unittest.main()