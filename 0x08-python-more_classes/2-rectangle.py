#!/usr/bin/python3
'''
An empty class Rectangle
'''


class Rectangle:
    '''Defining the empty class'''

    def __init__(self, width=0, height=0):
        '''the init method'''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''width getter method'''

        return self.__width

    @width.setter
    def width(self, value):
        '''width setter method'''

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        '''height getter method'''

        return self.__height

    @height.setter
    def height(self, value):
        '''height setter method'''

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        '''returns the rectangle area'''

        return self.__height * self.__width

    def perimeter(self):
        '''returns the rectangle perimeter'''

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
