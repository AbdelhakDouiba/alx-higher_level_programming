#!/usr/bin/python3
'''
This is "4-inherits_from" Module
inherits_from() - returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
'''


def inherits_from(obj, a_class) -> bool:
    '''returns True if the object is an instance of a class that inherited
       (directly or indirectly) from the specified class ; otherwise False.
    '''

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
