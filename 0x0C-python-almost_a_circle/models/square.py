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

    def __str__(self):
        """Square Object String"""

        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.height))
