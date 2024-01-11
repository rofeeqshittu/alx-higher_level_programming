#!/usr/bin/python3
""" Contains a defined Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self._Rectangle__x, self._Rectangle__y,
                self.size)
