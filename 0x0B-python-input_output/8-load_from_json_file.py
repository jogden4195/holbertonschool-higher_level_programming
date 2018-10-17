#!/usr/bin/python3
""" Module that creates an Obj from a JSON file """
import json


def load_from_json_file(filename):
    with open(filename, encoding='utf-8') as a_file:
        return json.load(a_file)
