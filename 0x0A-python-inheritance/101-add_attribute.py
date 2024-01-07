#!/usr/bin/python3
"""
    Class that add attribute
"""


def add_attribute(obj, attribute, value):
    """ Add attribute to an object if it's possible """

    if not hasattr(obj, "__dict__") and not hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
