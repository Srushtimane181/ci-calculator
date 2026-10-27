
import unittest
from calc_service import multiply, subtract

class CalculatorTests(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

if __name__ == "__main__":
    unittest.main()
