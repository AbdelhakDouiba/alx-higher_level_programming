#!/usr/bin/python3
'''
Square class with some operations
'''


class Square:
    '''Square class with some operations to claculate the area and
       store the size of the square

        Attributes:
            __size: size of the sqaure
    '''
    def __init__(self, size: int = 0) -> None:
        '''Square class

            Args:
                size: size of the sqaure
        '''
        self.size = size

    @property
    def size(self):
        '''size getter'''
        return self.__size

    @size.setter
    def size(self, size):
        '''size setter'''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Calculate the area of the square

            Returns:
                the area of the square
        '''
        return self.__size * self.__size
