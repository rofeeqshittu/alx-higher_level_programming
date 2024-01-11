#!/usr/bin/python3
""" Contains a defined Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self._Rectangle__x, self._Rectangle__y,
                self.size)

    # The update method
    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # The to_dictionary method
    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
