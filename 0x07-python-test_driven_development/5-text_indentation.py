#!/usr/bin/python3
"""
    Contains a text_indentation(text) function that prints something
"""


def text_indentation(text):
    """ Prints a text with 2 new lines after each of these characters:
        ., ? and : """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ".?:"
    buffer = ""

    for char in text:
        buffer += char
        if char in punctuation:
            print(buffer.strip())
            print()
            buffer = ""

    if buffer:
        print(buffer.strip())
