#!/usr/bin/python3

"""
A module Square contain a Square class.
"""


class Square:
    """ Square class that returns area of square. """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize with position & optional size.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Area of square."""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
            return

        [print("") for i in range(self.__position[1])]
        for _ in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
