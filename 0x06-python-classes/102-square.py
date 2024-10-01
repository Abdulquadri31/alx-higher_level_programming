#!/usr/bin/python3
class Square:
    """Defines a square with size validation and comparison based on area."""

    def __init__(self, size=0):
        """Initialize the square with size.

        Args:
            size (int or float): The size of the square, default is 0.

        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int or float): The size to be set.

        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if the area of this square is equal to another square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if the area of this square is not equal to another square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area of this square is less than another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of this square is less than or equal to another square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area of this square is greater than another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of this square is greater than or equal to another square."""
        return self.area() >= other.area()
