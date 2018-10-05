#!/usr/bin/python3
""" Module to add two integers
"""


def add_integer(a, b=98):
    """ add_integer - adds 2 integers

    Args:
        a (int): The first integer we are adding
        b (int): The second integer we are adding

    Returns:
        the sum of a and b

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
