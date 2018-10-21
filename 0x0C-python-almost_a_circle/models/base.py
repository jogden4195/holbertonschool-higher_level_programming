#!/usr/bin/python3
import json


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
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)
