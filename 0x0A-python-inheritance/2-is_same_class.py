#!/usr/bin/python3
'''
This is "2-is_same_class" Module
return True if an object is an instance of a given class
'''


def is_same_class(obj, a_class):
    '''returns True if the object is exactly an instance
       f the specified class ; otherwise False.
    '''

    return type(obj) is a_class
