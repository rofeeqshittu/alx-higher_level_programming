#!/usr/bin/python3
""" Contains append_write function """


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file """

    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
