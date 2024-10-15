#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a file.
"""
import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


filename = "add_item.json"

# Check if file exists, load the list if it does, or create an empty list
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add the arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
