#!/usr/bin/python3
"""
This is "10-student" module
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initialization"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student
           instance (same as 8-class_to_json.py)"""

        json_value = {}

        if hasattr(self, "__dict__"):
            if attrs is None:
                return self.__dict__

            for val in attrs:
                if val in self.__dict__:
                    json_value[val] = self.__dict__[val]

        return json_value
