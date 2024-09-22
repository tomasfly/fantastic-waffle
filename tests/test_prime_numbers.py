import unittest
from prime_numbers import is_prime

class PrimeNumbersTestCase(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(16))
        self.assertFalse(is_prime(18))
        self.assertFalse(is_prime(20))
        self.assertFalse(is_prime(21))
        self.assertFalse(is_prime(22))
        self.assertFalse(is_prime(24))
        self.assertFalse(is_prime(25))
        self.assertFalse(is_prime(26))
        self.assertFalse(is_prime(27))
        self.assertFalse(is_prime(28))
        self.assertFalse(is_prime(30))

if __name__ == '__main__':
    unittest.main()