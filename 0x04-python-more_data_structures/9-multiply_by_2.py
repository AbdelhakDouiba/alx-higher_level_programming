#!/usr/bin/python3
def multiply_by_2(a_dictionary: dict) -> dict:
    my_dictionary = {}
    for key, value in a_dictionary.items():
        my_dictionary[key] = value * 2
    return my_dictionary
