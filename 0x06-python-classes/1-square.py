#!/usr/bin/python3
"""
Module that defines a Square class.
"""

class Square:
    """
    A class that defines a square with a private instance attribute: size.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
