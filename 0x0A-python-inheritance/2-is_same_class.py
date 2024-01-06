#!/usr/bin/python3
"""
    Contains a function that returns True if obect is an instance
"""


def is_same_class(obj, a_class):
    """ Returns True if the object is exactly an instance of the class """

    return type(obj) is a_class
