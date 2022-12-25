#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):

        """This is function to test unit tests
        SO we are going to do so
        Here we fulfill the docstring string length requirement
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([20, 10, 40, 200]), 200)
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
