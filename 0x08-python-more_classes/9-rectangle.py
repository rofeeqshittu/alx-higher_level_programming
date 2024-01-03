#!/usr/bin/python3
"""
    Contains an defined Rectangle class
"""


class Rectangle:
    """ A defined rectangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Calc the area of the rectangle """

        return self.__width * self.__height

    def perimeter(self):
        """ Calc the perimeter of the rectangle """

        perim = 0
        if self.__height == 0 or self.height == 0:
            perim = 0
        else:
            perim = 2 * (self.__height + self.__width)

        return perim

    def __str__(self):
        rect_str = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for _ in range(self.__height):
                rect_str += str(self.print_symbol) * self.__width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns biggest rectangle """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Return new rectangle instance """

        new_rect = cls(size, size)
        return new_rect
