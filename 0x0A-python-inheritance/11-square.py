#!/usr/bin/python3
'''
This is "11-square" Module
Square - an inherited class from Rectangle class
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''Square class'''

    def __init__(self, size):
        '''initiliing the Square class'''

        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        '''Calculate the area'''

        return self.__size ** 2

    def __str__(self):
        '''The string of the class Square'''

        return "[Square] {}/{}".format(self.__size, self.__size)
