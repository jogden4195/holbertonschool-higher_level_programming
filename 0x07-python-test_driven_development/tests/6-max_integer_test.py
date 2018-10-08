#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ TestMaxInteger - unittest for max_integer function
    """
    def test_values(self):
        """test_values - tests return values for max_integer
        """
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([1, 5, 3, 2, 6, 3, 9]), 9)
        self.assertEqual(max_integer([9, 3, 6, 2, 3, 5, 1]), 9)
        self.assertEqual(max_integer([-4, -9, 5, -2, 3, 1]), 5)
        self.assertEqual(max_integer([-1, 3, 4, 5, 5]), 5)
        self.assertEqual(max_integer([1]), 1)

    def test_errors(self):
        """test_errors - tests exceptions raised for max_integer
        """
        with self.assertRaises(TypeError):
            max_integer([1, "Listen!", 3])

if __name__ == '__main__':
    unittest.main()
