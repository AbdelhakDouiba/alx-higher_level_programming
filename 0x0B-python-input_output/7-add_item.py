#!/usr/bin/python3
"""
This is "7-add_item" module
adds all arguments to a Python list, and then save them to a file
"""


from sys import argv
from os import path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_json():
    """adds all arguments to a Python list, and then save them to a file"""

    old_data = []

    if path.exists("./add_item.json"):
        try:
            old_data = load_from_json_file("add_item.json")
        except BaseException:
            pass

    new_data = old_data + argv[1:]

    save_to_json_file(new_data, "add_item.json")


if __name__ == "__main__":
    add_json()
