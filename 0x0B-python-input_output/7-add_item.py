#!/usr/bin/python3
"""
This is "7-add_item" module
adds all arguments to a Python list, and then save them to a file
"""


from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

with open("add_item.json", encoding="UTF-8") as ff:
    pass
try:
    old_data = load_from_json_file("add_item.json")
except:
    old_data = []

if type(old_data) is not list:
    old_data = list(old_data)

new_data = old_data + argv[1:]

save_to_json_file(new_data, "add_item.json")
