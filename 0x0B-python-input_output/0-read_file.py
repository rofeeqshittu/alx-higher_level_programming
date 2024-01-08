#!/usr/bin/python3
""" Contain a read_file function """


def read_file(filename=""):
    """ Read a text file (UTF8) and prints it to stdout """

    with open(filename, encoding='UTF8') as f:
        print(f.read(), end="")
