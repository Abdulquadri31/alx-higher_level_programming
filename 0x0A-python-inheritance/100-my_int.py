#!/usr/bin/python3
"""
This module defines a MyInt class that inherits from int and
inverts the == and != operators.
"""


class MyInt(int):
    """
    A rebel integer class that inverts == and != operators.
    """

    def __eq__(self, other):
        """
        Invert the behavior of the equality operator.

        Args:
            other (int): The integer to compare.

        Returns:
            bool: True if self is not equal to other, otherwise False.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Invert the behavior of the inequality operator.

        Args:
            other (int): The integer to compare.

        Returns:
            bool: True if self is equal to other, otherwise False.
        """
        return super().__eq__(other)
