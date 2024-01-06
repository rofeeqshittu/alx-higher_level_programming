#!/usr/bin/python3
"""
    Contains inherits_from()
"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that inherited """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
