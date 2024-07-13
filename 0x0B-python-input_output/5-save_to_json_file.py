#!/usr/bin/python3
"""
This is "5-save_to_json_file.py" Module
"""


def save_to_json_file(my_obj, filename: str):
    """writes an Object to a text file, using a JSON representation"""

    import json

    with open(filename, "w", encoding="UTF-8") as json_file:
        json.dump(my_obj, json_file)
