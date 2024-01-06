#!/usr/bin/python3
"""
    Module containing lookup() function
"""


def lookup(obj):
    """ Returns the list of available attributes and methods of an object """

    return [attr for attr in dir(obj) if not
            callable(getattr(obj, attr)) or
            hasattr(obj, attr)]
