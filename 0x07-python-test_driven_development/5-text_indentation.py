#!/usr/bin/python3
"""
This module provides a function to print text with 2 new lines after each '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_space = False

    for char in text:
        if skip_space and char == ' ':
            continue
        skip_space = False

        result += char
        if char in ['.', '?', ':']:
            result += "\n\n"
            skip_space = True

    print(result.strip())
