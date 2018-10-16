#!/usr/bin/python3
""" Module that checks if obj is subclass """


def inherits_from(obj, a_class):
    """
    inherits_from - Checks if an obj is a subclass
    """
    if issubclass(type(obj), a_class) and (type(obj) != a_class):
        return True
    else:
        return False
