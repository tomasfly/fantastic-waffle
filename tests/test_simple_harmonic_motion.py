import unittest
from src.simple_harmonic_motion import calculate_amplitude, calculate_period, calculate_frequency

class SimpleHarmonicMotionTestCase(unittest.TestCase):
    def test_calculate_amplitude(self):
        # Test cases for calculate_amplitude function
        self.assertEqual(calculate_amplitude(5, 2), 3)
        self.assertEqual(calculate_amplitude(10, 4), 6)
        self.assertEqual(calculate_amplitude(15, 7), 8)
    
    def test_calculate_period(self):
        # Test cases for calculate_period function
        self.assertEqual(calculate_period(5, 2), 1.5707963267948966)
        self.assertEqual(calculate_period(10, 4), 0.7853981633974483)
        self.assertEqual(calculate_period(15, 7), 0.4487989505128276)
    
    def test_calculate_frequency(self):
        # Test cases for calculate_frequency function
        self.assertEqual(calculate_frequency(5, 2), 0.6366197723675814)
        self.assertEqual(calculate_frequency(10, 4), 1.2732395447351628)
        self.assertEqual(calculate_frequency(15, 7), 2.2222222222222223)

if __name__ == '__main__':
    unittest.main()