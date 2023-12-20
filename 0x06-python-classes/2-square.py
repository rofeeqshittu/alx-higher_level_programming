#!/usr/bin/python3

"""
A class Square defined by instance attribute size.
"""


class Square:
    """ Square class with private instance attribute size. """

    def __init__(self, size=0):
        """Initialization method with optional size."""

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
