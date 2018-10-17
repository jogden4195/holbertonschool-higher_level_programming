#!/usr/bin/python3
""" Module for returning a dict desc for JSON serialization """


def class_to_json(obj):
    """ class_to_json - returns the dict desctiption """
    return obj.__dict__
