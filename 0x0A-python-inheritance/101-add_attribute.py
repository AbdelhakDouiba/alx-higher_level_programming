#!/usr/bin/python3
'''
This is "101-add_attribute" Module
'''


def add_attribute(obj, attr, value):
    '''adds a new attribute to an object if it’s possible'''

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if attr not in obj.__dict__.keys():
        obj.__dict__[attr] = value
