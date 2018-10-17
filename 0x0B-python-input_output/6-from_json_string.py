#!/usr/bin/python3
""" Module that returns an obj represented by a JSON str """
import json


def from_json_string(my_str):
    """ from_json_string - returns obj represented by JSON str """
    return json.loads(my_str)
