#!/usr/bin/python3
"""
This module defines a class BaseGeometry with methods for geometric operations.
"""

class BaseGeometry:
    """
    A class that represents basic geometric operations.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer and greater than 0.

        Args:
            name (str): The name of the parameter (assumed to be a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
