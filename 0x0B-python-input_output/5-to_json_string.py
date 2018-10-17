#!/usr/bin/python3
""" Module that returns the JSON rep of an obj """
import json


def to_json_string(my_obj):
    """ to_json_string - returns the JSON rep of an obj """
    return json.dumps(my_obj)
