#!/usr/bin/python3
""" Module for checking if object is instance of given class """


def is_same_class(obj, a_class):
    """ is_same_class - checks if object is instance of class

    Arguments:
        obj (object): object we are checking
        a_class (class): class we are seeing if obj is an instance of

    Returns:
        Bool

    """
    return (type(obj) is a_class)
