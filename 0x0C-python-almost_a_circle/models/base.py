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
