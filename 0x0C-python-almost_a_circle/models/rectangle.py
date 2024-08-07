#!/usr/bin/python3
"""
This is "rectangle" Module
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Intialization Rectangle object"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Calculate the area"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        symbol = "#"
        y = "\n" * self.y
        row = " " * self.x + symbol * self.width + "\n"
        rectangle = y + row * self.height

        print(rectangle, end="")

    def __str__(self):
        """Object string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """assigns an argument to attributes"""
        attrs = ["id", "width", "height", "x", "y"]

        if len(args) > 0 and args is not None:
            for attribute, value in zip(attrs, args):
                setattr(self, attribute, value)

        if len(kwargs) > 0 and kwargs is not None:
            for attribute, value in kwargs.items():
                setattr(self, attribute, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
