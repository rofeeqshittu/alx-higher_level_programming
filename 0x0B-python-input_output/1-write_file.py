#!/usr/bin/python3
""" Contains a write_file function """


def write_file(filename="", text=""):
    """ Write to a text file (UTF8) and return the number of char written"""

    with open(filename, 'w', encoding='UTF8') as f:
        char_count = f.write(text)
    return char_count
