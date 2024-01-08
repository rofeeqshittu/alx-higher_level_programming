#!/usr/bin/python3
"""
    Contains a class that inherit
"""


class BaseGeometry:
    """ A geometry class """

    def area(self):
        """ Raise Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer validator """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value


class Rectangle(BaseGeometry):
    """ Class inherits from BaseGeometry """

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """ Class inherit from Rectangle """

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = self.integer_validator("size", size)

     def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
