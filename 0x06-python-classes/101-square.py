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
    def __init__(self, size: int = 0, position: tuple = (0, 0)) -> None:
        '''Square class

            Args:
                size: size of the sqaure
        '''
        self.size = size
        self.position = position

    @property
    def size(self) -> int:
        '''size getter'''
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        '''size setter'''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self) -> tuple:
        '''position getter'''
        return self.__position

    @position.setter
    def position(self, value: tuple) -> None:
        '''position setter'''
        if type(value) is tuple and len(value) == 2 and \
            type(value[0]) is int and value[0] >= 0 and \
                type(value[1]) is int and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''Calculate the area of the square

            Returns:
                the area of the square
        '''
        return self.__size * self.__size

    def my_print(self):
        '''prints in stdout the square with the character #'''
        if self.__size <= 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        '''the class string'''
        re_str = ""
        if self.__size > 0:
            re_str += "\n" * self.__position[1]
            for i in range(self.__size):
                re_str += " " * self.__position[0] + "#" * self.__size + "\n"
        return re_str[:-1]
