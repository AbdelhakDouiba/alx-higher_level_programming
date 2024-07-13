#!/usr/bin/python3
"""
This is "6-load_from_json_file" Module
"""


def load_from_json_file(filename: str):
    """creates an Object from a 'JSON file'"""

    import json

    with open(filename, encoding="UTF-8") as my_file:
        data = json.load(my_file)
    return data
