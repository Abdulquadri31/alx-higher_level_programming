#!/usr/bin/python3
"""
Defines a Student class.
"""


class Student:
    """
    A class that defines a student by:
    - first_name
    - last_name
    - age
    """
    
    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        
        If attrs is a list of strings, only the attributes listed in attrs
        are included in the dictionary. Otherwise, all attributes are included.

        Args:
            attrs (list): A list of strings representing attribute names.
        
        Returns:
            dict: A dictionary containing the specified attributes of
                  the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__
