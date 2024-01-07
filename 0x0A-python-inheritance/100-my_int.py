#!/usr/bin/python3
"""
    Contain MyInt
"""


class MyInt(int):
    """ Inherits from int  """

    def __eq__(self, other):
        """ Inverted == operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Inverted != operator """
        return super().__eq__(other)
