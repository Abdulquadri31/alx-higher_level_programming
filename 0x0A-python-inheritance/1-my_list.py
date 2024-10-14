#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and contains a method to print the list in sorted order.
"""

class MyList(list):
    """
    MyList inherits from list with a method to print the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        Assumes all elements in the list are of type int.
        """
        print(sorted(self))
