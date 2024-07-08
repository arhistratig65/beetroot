import unittest

from calc import Calc


class TestCalc(unittest.TestCase):

    def setUp(self):
        pass

    def test_of_test(self):
        self.assertTrue(True)

    def test_add(self):
        result = Calc.add(2, 2)
        self.assertEqual(result, 4)

    def test_sub(self):
        result = Calc.sub(10, 5)
        self.assertEqual(result, 5)

    def test_sub_negative(self):
        result = Calc.sub(5, 10)
        self.assertEqual(result, -5)

    def test_mul(self):
        result = Calc.mul(3, 4)
        self.assertEqual(result, 12)

    def test_pow(self):
        result = Calc.pow(2, 3)
        self.assertEqual(result, 8)

    def test_div(self):
        result = Calc.div(10, 2)
        self.assertEqual(result, 5)

    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            Calc.div(10, 0)

    def test_floordiv(self):
        result = Calc.floordiv(10, 3)
        self.assertEqual(result, 3)

    def test_floordiv_by_zero(self):
        with self.assertRaises(ValueError):
            Calc.floordiv(10, 0)

    def test_mod(self):
        result = Calc.mod(10, 3)
        self.assertEqual(result, 1)

    def test_mod_by_zero(self):
        with self.assertRaises(ValueError):
            Calc.mod(10, 0)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
