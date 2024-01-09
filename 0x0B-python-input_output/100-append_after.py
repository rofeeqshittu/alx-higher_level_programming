#!/usr/bin/python3
""" Defines append_after function """


def append_after(filename="", search_string="", new_string=""):
    """ Function inserts a line of text to a file, after each line
    containing a specific string """

    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
