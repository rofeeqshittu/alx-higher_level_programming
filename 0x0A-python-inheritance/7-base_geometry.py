#!/usr/bin/python3
"""
    Contains a class BaseGeometry
"""


class BaseGeometry:
    """ A geometry class """

    def __init__(self):
        super().__init()

    def area(self):
        """ Raise Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer validator """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        return value
