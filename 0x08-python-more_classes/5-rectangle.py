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

    def __str__(self):
        '''class's string'''
        s = ''
        if self.__width == 0 or self.__height == 0:
            return s
        for i in range(self.__height):
            s += '#' * self.__width
            if i < self.__height - 1:
                s += '\n'
        return s

    def __repr__(self):
        '''String representation'''

        return f"Rectangle({self.__width:d}, {self.__height:d})"

    def __del__(self):
        '''Print the message 'Bye rectangle...' when an object is deleted'''

        print("Bye rectangle...")
