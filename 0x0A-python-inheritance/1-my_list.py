#!/usr/bin/python3
"""
    Contains MyList function
"""


class MyList(list):
    """ This class inherits from class list """

    def __init__(self):
        " initializes the object """
        super().__init()

    def print_sorted(self):
        """ Prints a sorted list given """
        print(sorted(self))
