#!/usr/bin/python3
'''
This is "3-is_kind_of_class" Module
is_kind_of_class() - returns True if the object is an instance of, or if
the object is an instance of a class that inherited from, the specified
class ; otherwise False.
'''


def is_kind_of_class(obj, a_class) -> bool:
    '''returns True if the object is an instance of, or if the object is an
       instance of a class that inherited from, the specified class ; otherwise
       False.
    '''

    return isinstance(obj, a_class)
