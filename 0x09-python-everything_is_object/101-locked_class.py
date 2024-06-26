#!/usr/bin/python3
'''
This is "101-locked_class" Module
LockedClass -  that prevents the user from dynamically creating new
instance attributes, except if the new instance attribute is called
first_name.
'''

class LockedClass:
    __slots__ = ("first_name", )
