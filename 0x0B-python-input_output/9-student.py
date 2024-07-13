#!/usr/bin/python3
"""
This is "9-student" module
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initialization"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student
           instance (same as 8-class_to_json.py)"""

        if hasattr(self, "__dict__"):
            return self.__dict__
        return {}
