#!/usr/bin/python3
'''
This is "8-rectangle" Module
Rectangle - a class that inherits from BaseGeometry class
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class'''

    def __init__(self, width, height):
        '''initilize Rectangle with the attributes: width and height

            Args:
                width: the width
                height: the height
        '''

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
