#!/usr/bin/python3
""" Module for lookup function """


def lookup(obj):
    """ lookup - returns attributes/methods of an object

    Args:
        @obj - The object we are returning attributes for

    Returns:
        list of the object's attributes

    """
    return dir(obj)
