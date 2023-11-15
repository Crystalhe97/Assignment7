
import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        # finish
        pass

    def test_multiply(self):
        # finish
        pass

    def test_divide(self):
        # finish
        pass

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()