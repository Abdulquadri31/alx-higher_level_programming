#!/usr/bin/python3
"""
Inserts a line of text after each line containing a specific string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a new_string after each line containing search_string in the file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in the file.
        new_string (str): The string to insert after each line containing search_string.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()  # Read all lines from the file

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)  # Write the original line
            if search_string in line:  # Check if the search_string is in the line
                file.write(new_string)  # Write the new_string after the line
