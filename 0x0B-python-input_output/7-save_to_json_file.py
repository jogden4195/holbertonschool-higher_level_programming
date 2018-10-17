#!/usr/bin/python3
""" Module that writes an object to a .txt """
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file - writes an obj to a .txt """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
