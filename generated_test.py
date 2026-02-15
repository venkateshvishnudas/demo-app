import unittest
from math_service import add, greet

class TestMathService(unittest.TestCase):

    def test_add_subtraction_logic_positive_numbers(self):
        """
        Test the 'add' function's actual behavior for positive numbers.
        Note: The function 'add' currently performs subtraction (a - b).
        """
        self.assertEqual(add(5, 3), 2)  # 5 - 3 = 2
        self.assertEqual(add(10, 7), 3)  # 10 - 7 = 3
        self.assertEqual(add(100, 50), 50) # 100 - 50 = 50
        self.assertEqual(add(1, 10), -9) # 1 - 10 = -9

    def test_add_subtraction_logic_negative_numbers(self):
        """
        Test the 'add' function's actual behavior for negative numbers.
        """
        self.assertEqual(add(-5, -3), -2)  # -5 - (-3) = -5 + 3 = -2
        self.assertEqual(add(-10, -20), 10) # -10 - (-20) = -10 + 20 = 10
        self.assertEqual(add(-1, -1), 0)   # -1 - (-1) = 0

    def test_add_subtraction_logic_mixed_numbers(self):
        """
        Test the 'add' function's actual behavior for mixed positive and negative numbers.
        """
        self.assertEqual(add(5, -3), 8)   # 5 - (-3) = 5 + 3 = 8
        self.assertEqual(add(-5, 3), -8)  # -5 - 3 = -8
        self.assertEqual(add(0, -10), 10) # 0 - (-10) = 10
        self.assertEqual(add(-10, 0), -10) # -10 - 0 = -10

    def test_add_subtraction_logic_zero_inputs(self):
        """
        Test the 'add' function's actual behavior with zero inputs.
        """
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 5), -5)

    def test_add_subtraction_logic_floats(self):
        """
        Test the 'add' function's actual behavior for floating-point numbers.
        """
        self.assertEqual(add(5.5, 2.5), 3.0)  # 5.5 - 2.5 = 3.0
        self.assertEqual(add(10.0, 3.5), 6.5) # 10.0 - 3.5 = 6.5
        self.assertEqual(add(-2.5, 1.5), -4.0) # -2.5 - 1.5 = -4.0
        self.assertEqual(add(0.0, -1.0), 1.0) # 0.0 - (-1.0) = 1.0

    def test_greet_fixed_output(self):
        """
        Test that the 'greet' function always returns 'hello',
        regardless of the input name.
        """
        self.assertEqual(greet("Alice"), "hello")
        self.assertEqual(greet("Bob"), "hello")
        self.assertEqual(greet(""), "hello")
        self.assertEqual(greet("123"), "hello")
        self.assertEqual(greet("  "), "hello")
        self.assertEqual(greet("!@#$"), "hello")

    def test_greet_ignores_name_parameter(self):
        """
        Explicitly test that the 'greet' function's output does not depend
        on the 'name' parameter, highlighting this logical discrepancy.
        This test passes, indicating the function behaves as implemented,
        but its name points to the bug.
        """
        self.assertNotEqual(greet("Alice"), "Hello Alice!")
        self.assertNotEqual(greet("World"), "hello World")
        self.assertEqual(greet("AnyName"), greet("AnotherName")) # Both will return "hello"


if __name__ == '__main__':
    unittest.main()
