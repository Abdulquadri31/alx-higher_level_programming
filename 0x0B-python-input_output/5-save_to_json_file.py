#!/usr/bin/python3
"""
Module that defines the function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (any): The object to save to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
