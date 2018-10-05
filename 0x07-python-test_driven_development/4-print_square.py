#!/usr/bin/python3
"""Module to print a square
"""


def print_square(size):
    """ print_square - prints a square with the character '#'

    Args:
        size (int): size length of the square

    Return:
        None

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        row = '#' * size
        for i in range(size):
            print(row)
