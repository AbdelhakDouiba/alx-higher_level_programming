#!/usr/bin/python3
'''
This is 3-say_my_name Module
say_my_name - prints My name is <first name> <last name>
'''


def say_my_name(first_name: str, last_name: str = ""):
    '''prints My name is <first name> <last name>

        Args:
            first_name: first name string
            last_name: last name string
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print('My name is {} {}'.format(first_name, last_name))
