#!/usr/bin/python3
""" Module that checks if object is instance/sublass of class """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class - checks if obj is instance or subclass

    Arguments:
        obj (object): object we are checking
        a_class (class): class we are seeing if
    """
    return isinstance(obj, a_class)
