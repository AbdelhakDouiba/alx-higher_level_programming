#!/usr/bin/python3
'''
This 4-print_square Module
print_square - prints a square with the character #.
'''


def print_square(size: int):
    '''a function that prints a square with the character #.

        Args:
            size: the size of the square
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
