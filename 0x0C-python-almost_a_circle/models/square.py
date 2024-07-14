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

    @property
    def size(self):
        """size getter"""

        return self.width

    @size.setter
    def size(self, value):
        """size setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """Square Object String"""

        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.height))

    def update(self, *args, **kwargs):
        """assigns attributes"""
        attrs = ["id", "size", "x", "y"]

        if args is not None and len(args) > 0:
            for attribute, value in zip(attrs, args):
                setattr(self, attribute, value)

        if kwargs is not None and len(kwargs) > 0:
            for attribute, value in kwargs.items():
                setattr(self, attribute, value)

    def to_dictionary(self):
        """eturns the dictionary representation of a Square"""

        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
