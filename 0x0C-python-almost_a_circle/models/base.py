#!/usr/bin/python3
"""
This is "base" module
"""


import json


class Base:
    """A class named Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization for the object"""

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        unique_dicts = {}
        for dictionary in list_dictionaries:
            unique_dicts[dictionary['id']] = dictionary

        unique_list = list(unique_dicts.values())
        return json.dumps(unique_list)
