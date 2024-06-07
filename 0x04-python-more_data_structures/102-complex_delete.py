#!/usr/bin/python3
def complex_delete(a_dictionary: dict, value: str) -> dict:
    del_list = []
    for key, val in a_dictionary.items():
        if val == value:
            del_list += [key]
    for key in del_list:
        del a_dictionary[key]
    return a_dictionary
