#!/usr/bin/python3
"""
Module that defines the function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the file to load from.

    Returns:
        any: The Python object represented by the JSON file content.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
