#!/usr/bin/python3
"""
This is "3-to_json_string" Module
"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""

    import json
    return json.dumps(my_obj)
