#!/usr/bin/python3
""" Contains class_to_json function """


def class_to_json(obj):
    """ Returns the dictionary description with a simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object """

    attribute_dict = {}
    for attr_name in dir(obj):
        if not callable(getattr(obj, attr_name)) \
                and not attr_name.startswith("__"):
            attr_value = getattr(obj, attr_name)

            if isinstance(attr_value, (list, dict, str, int, bool)):
                attribute_dict[attr_name] = attr_value

    return attribute_dict
