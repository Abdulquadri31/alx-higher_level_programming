import math


class MagicClass:
    """
    A class that defines a circle by its radius.
    """

    def __init__(self, radius=0):
        """
        Initializes the MagicClass with a radius.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0  # Initialize the private radius attribute

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius  # Set the radius attribute

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return (self.__radius ** 2) * math.pi  # Area = π * r²

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius  # Circumference = 2 * π * r
