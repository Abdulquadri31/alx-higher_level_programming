#!/usr/bin/python3
class Square:
    """A class that defines a square."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position attributes.

        Args:
            size (int): The size of the square, default is 0.
            position (tuple): The position to start printing the square, default is (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value checks.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with type checks.

        Args:
            value (tuple): The position to start printing the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #, or an empty line if size is 0."""
        if self.__size == 0:
            print("")
        else:
            # Print new lines for position[1] vertical offset
            for _ in range(self.__position[1]):
                print("")
            # Print the square with horizontal space based on position[0]
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
