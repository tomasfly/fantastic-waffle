import unittest
from src.newtons_laws import *

class TestNewtonsLaws(unittest.TestCase):
    def test_first_law(self):
        # Test cases for Newton's First Law of Motion
        self.assertTrue(first_law(0, 0))
        self.assertFalse(first_law(10, 0))
        self.assertFalse(first_law(0, 10))
        self.assertFalse(first_law(10, 10))

    def test_second_law(self):
        # Test cases for Newton's Second Law of Motion
        self.assertEqual(second_law(0, 0), 0)
        self.assertEqual(second_law(10, 0), 0)
        self.assertEqual(second_law(0, 10), 0)
        self.assertEqual(second_law(10, 10), 100)

    def test_third_law(self):
        # Test cases for Newton's Third Law of Motion
        self.assertTrue(third_law(10, -10))
        self.assertTrue(third_law(-10, 10))
        self.assertFalse(third_law(10, 10))
        self.assertFalse(third_law(-10, -10))

if __name__ == '__main__':
    unittest.main()