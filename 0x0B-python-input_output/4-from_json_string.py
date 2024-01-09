#!/usr/bin/python3
""" Contain the from_json_string function """
import json


def from_json_string(my_str):
    """ Returns an object (Python data structure) represented by a JSON"""
    return json.loads(my_str)
