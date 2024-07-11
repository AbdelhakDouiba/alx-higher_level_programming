#!/usr/bin/python3
'''
This is "7-base_geometry" Module
BaseGeometry - a class
'''


class BaseGeometry:
    '''Base Geometry class'''

    def area(self):
        '''Calculate the area'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''integer validator'''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
