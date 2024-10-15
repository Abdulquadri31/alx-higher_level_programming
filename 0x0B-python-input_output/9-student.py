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

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.
        
        Returns:
            dict: A dictionary containing all attributes of the Student instance.
        """
        return self.__dict__
