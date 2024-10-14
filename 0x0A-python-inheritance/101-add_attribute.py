#!/usr/bin/python3
"""
This module defines a function to add a new attribute to an object
if possible.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute should be added.
        attribute (str): The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
