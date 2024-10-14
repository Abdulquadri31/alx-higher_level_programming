#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a specified class, or if the object is an instance of a class that
inherited from the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        True if obj is an instance or a subclass instance of a_class,
        otherwise False.
    """
    return isinstance(obj, a_class)
