#!/usr/bin/python3
'''
Square class with size attribute
'''


class Square:
    '''Square class defined with private attribute size'''
    def __init__(self, size=0):
        '''initializing the object with private attribute size

            args:
                size: private attribute that hold the size of the square
        '''
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
