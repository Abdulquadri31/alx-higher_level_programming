#!/usr/bin/python3
"""
Module that defines a Square class.
"""


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (float or int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compares if two squares have the same area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares if two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if this square is smaller than another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if this square is smaller than or equal to another square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if this square is larger than another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if this square is larger than or equal to another square."""
        return self.area() >= other.area()
