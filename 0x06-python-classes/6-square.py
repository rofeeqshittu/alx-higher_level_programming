#!/usr/bin/python3

"""
A module Square contain a Square class.
"""


class Square:
    """ Square class that returns area of square. """

    def __init__(self, size=0, position=(0, 0)):
        """Initialization method with position & optional size."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set size."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Area of square."""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
