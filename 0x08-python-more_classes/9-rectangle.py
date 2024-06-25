#!/usr/bin/python3
'''
An empty class Rectangle
'''


class Rectangle:
    '''Defining the empty class'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''the init method'''

        self.width = width
        self.height = height

        type(self).number_of_instances = self.number_of_instances + 1

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
        symbol = str(self.print_symbol)
        if self.__width == 0 or self.__height == 0:
            return s
        for i in range(self.__height):
            s += symbol * self.__width
            if i < self.__height - 1:
                s += '\n'
        return s

    def __repr__(self):
        '''String representation'''

        return f"Rectangle({self.__width:d}, {self.__height:d})"

    def __del__(self):
        '''Print the message 'Bye rectangle...' when an object is deleted'''

        print("Bye rectangle...")

        type(self).number_of_instances = self.number_of_instances - 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest rectangle based on the area'''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        '''returns a new Rectangle instance with width == height == size'''

        return cls(size, size)
