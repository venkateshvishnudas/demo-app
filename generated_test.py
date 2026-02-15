import unittest
from math_service import add, greet

class TestMathService(unittest.TestCase):

    # --- Tests for the 'add' function ---
    # The current implementation of 'add' returns a - b, which is incorrect for addition.
    # These tests are designed to fail and expose this logic bug by asserting the correct sum.

    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        # Expected: 5 + 3 = 8
        # Actual (bug): 5 - 3 = 2
        self.assertEqual(add(5, 3), 8, "Bug: add(5, 3) should be 8, but current implementation performs subtraction.")

    def test_add_negative_numbers(self):
        """Test addition of two negative numbers."""
        # Expected: -5 + (-3) = -8
        # Actual (bug): -5 - (-3) = -2
        self.assertEqual(add(-5, -3), -8, "Bug: add(-5, -3) should be -8, but current implementation performs subtraction.")

    def test_add_mixed_numbers(self):
        """Test addition of positive and negative numbers."""
        # Expected: 5 + (-3) = 2
        # Actual (bug): 5 - (-3) = 8
        self.assertEqual(add(5, -3), 2, "Bug: add(5, -3) should be 2, but current implementation performs subtraction.")
        # Expected: -5 + 3 = -2
        # Actual (bug): -5 - 3 = -8
        self.assertEqual(add(-5, 3), -2, "Bug: add(-5, 3) should be -2, but current implementation performs subtraction.")

    def test_add_with_zero(self):
        """Test addition involving zero."""
        # Expected: 0 + 7 = 7
        # Actual (bug): 0 - 7 = -7
        self.assertEqual(add(0, 7), 7, "Bug: add(0, 7) should be 7, but current implementation performs subtraction.")
        # Expected: 7 + 0 = 7
        # Actual (bug): 7 - 0 = 7 (This specific assertion passes even with the bug)
        self.assertEqual(add(7, 0), 7, "Bug: add(7, 0) should be 7.")
        # Expected: 0 + 0 = 0
        # Actual (bug): 0 - 0 = 0 (This specific assertion passes even with the bug)
        self.assertEqual(add(0, 0), 0, "Bug: add(0, 0) should be 0.")

    def test_add_floating_point_numbers(self):
        """Test addition of floating-point numbers."""
        # Expected: 2.5 + 1.5 = 4.0
        # Actual (bug): 2.5 - 1.5 = 1.0
        self.assertAlmostEqual(add(2.5, 1.5), 4.0, msg="Bug: add(2.5, 1.5) should be 4.0, but current implementation performs subtraction.")
        # Expected: 0.1 + 0.2 = 0.3
        # Actual (bug): 0.1 - 0.2 = -0.1
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, msg="Bug: add(0.1, 0.2) should be 0.3, but current implementation performs subtraction.")

    # --- Tests for the 'greet' function ---
    # The current implementation of 'greet' always returns "hello", ignoring the 'name' parameter.
    # These tests are designed to fail and expose this logic bug by asserting the expected personalized greeting.

    def test_greet_with_standard_name(self):
        """Test greeting with a typical name."""
        # Expected: "Hello, Alice!"
        # Actual (bug): "hello"
        self.assertEqual(greet("Alice"), "Hello, Alice!", "Bug: greet('Alice') should return a personalized greeting including the name.")
        self.assertEqual(greet("Bob"), "Hello, Bob!", "Bug: greet('Bob') should return a personalized greeting including the name.")

    def test_greet_empty_name(self):
        """Test greeting with an empty string as a name."""
        # Expected: "Hello, !" (assuming direct concatenation of an empty string, or similar handling)
        # Actual (bug): "hello"
        self.assertEqual(greet(""), "Hello, !", "Bug: greet('') should return a personalized greeting, even if name is empty.")

    def test_greet_name_with_spaces(self):
        """Test greeting with a name containing spaces."""
        # Expected: "Hello, John Doe!"
        # Actual (bug): "hello"
        self.assertEqual(greet("John Doe"), "Hello, John Doe!", "Bug: greet('John Doe') should include the full name in the greeting.")

    def test_greet_name_with_special_characters_and_numbers(self):
        """Test greeting with a name containing special characters and numbers."""
        # Expected: "Hello, User123_!"
        # Actual (bug): "hello"
        self.assertEqual(greet("User123_"), "Hello, User123_!", "Bug: greet('User123_') should include the name exactly as provided.")

if __name__ == '__main__':
    unittest.main()
