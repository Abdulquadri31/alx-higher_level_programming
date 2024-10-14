#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an area method that raises
an exception.
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
