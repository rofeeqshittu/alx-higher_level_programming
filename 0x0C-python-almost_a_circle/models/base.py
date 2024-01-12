#!/usr/bin/python3
""" Contain the Base class """
import json


class Base:
    """ Defines a Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """

        filename = cls.__name__ + ".json"
        obj_list = [] if list_objs is None else [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_list)

        with open(filename, 'w') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create() returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instance """

        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                data = file.read()
                obj_list = Base.from_json_string(data)
                return [cls.create(**obj) for obj in obj_list]
        except FileNotFoundError:
            return []
