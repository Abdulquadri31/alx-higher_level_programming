#!/usr/bin/python3
"""Unittests for max_integer([..]) function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_positive_integers(self):
        """Test a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        """Test a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test a list of mixed positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_float_values(self):
        """Test a list of float values"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_string_elements(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")

    def test_list_of_one_empty_list(self):
        """Test a list of one empty list"""
        self.assertEqual(max_integer([[]]), None)

    def test_none_argument(self):
        """Test None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
