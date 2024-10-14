#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initializes a square with size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        # Call the superclass (Rectangle) initializer with width and height as size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The description of the square.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
