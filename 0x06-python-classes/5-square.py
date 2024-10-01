#!/usr/bin/python3
"""
Module that defines a Square class.
"""

class Square:
    """
    A class that defines a square with a private instance attribute: size.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Using the setter method to initialize the size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The current area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character #.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return
        
        for _ in range(self.__size):
            print("#" * self.__size)
