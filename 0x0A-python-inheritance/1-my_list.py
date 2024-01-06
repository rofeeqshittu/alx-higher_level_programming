#!/usr/bin/python3
"""
    Contains MyList function
"""


class MyList(list):
    """ This class inherits from class list """

    def print_sorted(self):
        """ Prints a sorted list given """
        print(sorted(self))
