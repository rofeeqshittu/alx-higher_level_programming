#!/usr/bin/python3
"""
    Class that add attribute
"""


def add_attribute(obj, attribute, value):
    """ Add attribute to an object if it's possible """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
