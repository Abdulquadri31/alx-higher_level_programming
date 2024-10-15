#!/usr/bin/python3
"""
Function that returns the dictionary description for
JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON
    serialization of an object.
    
    Args:
        obj: An instance of a Class.
        
    Returns:
        A dictionary containing all serializable attributes of the object.
    """
    return obj.__dict__
