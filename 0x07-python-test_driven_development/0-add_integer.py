#!/usr/bin/python3
'''
This is add_integer module
define a simple add function
---> Expected inputs types : integer or float.
'''


def add_integer(a, b=98) -> int:
    '''Calculate the addition of a and b
        Returns: The addition of a and b (a + b)
    '''

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
