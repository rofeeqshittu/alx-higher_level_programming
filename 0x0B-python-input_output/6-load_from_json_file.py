#!/usr/bin/python3
""" Contains load_from_json_file function """
import json


def load_from_json_file(filename):
    """ Creates an Object from a "JSON file" """
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
