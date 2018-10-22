#!/usr/bin/python3
""" Module for Base class """
import json
from pathlib import Path


class Base:
    """ Base class - base of all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__ - initializes the base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string - returns JSON rep of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries is []:
            return json.dumps("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON str rep of list_objs to file"""
        filename = str(cls.__name__) + ".json"
        with open(filename, mode="w", encoding='utf-8') as a_file:
            if list_objs is None:
                text = cls.to_json_string([])
            else:
                list_o_dict = []
                for i in list_objs:
                    list_o_dict.append(cls.to_dictionary(i))
                text = cls.to_json_string(list_o_dict)
            a_file.write(text)

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string - returns list of JSON str rep """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create - returns an instance with all attrs already set """
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load_from_file - returns a list of instances """
        filename = str(cls.__name__) + ".json"
        path_to_file = Path(filename)
        a_list = []
        if path_to_file.is_file():
            with open(filename, mode='r', encoding='utf-8') as a_file:
                instances = cls.from_json_string(a_file.read())
                for i in instances:
                    a_list.append(cls.create(**i))
        return a_list
