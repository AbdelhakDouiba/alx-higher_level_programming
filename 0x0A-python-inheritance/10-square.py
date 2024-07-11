#!/usr/bin/python3
'''
This is "10-square" Module
Square - an inherited class from Rectangle class
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''Square class'''

    def __init__(self, size):
        '''initiliing the Square class'''

        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Calculate the area'''

        return self.__size ** 2
