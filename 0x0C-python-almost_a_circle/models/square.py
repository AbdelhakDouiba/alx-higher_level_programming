#!/usr/bin/python3
"""
This is "square" module
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class)"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of a Square object"""

        super().__init__(size, size, x, y, id)

        self.size = size

    @property
    def size(self):
        """size getter"""

        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
        self.__size = value

    def __str__(self):
        """Square Object String"""

        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.height))
