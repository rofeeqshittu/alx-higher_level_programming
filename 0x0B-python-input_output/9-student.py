#!/usr/bin/python3
""" Contains a class Student """


class Student:
    """ Defines a student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieve a dictionary representation of a Student instance """
        return vars(self)
