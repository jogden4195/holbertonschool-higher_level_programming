#!/usr/bin/python3
"""Module to edit a string
"""


def text_indentation(text):
    """ text_indentation - prints a text with 2 lines after
    the characters ``.``, ``?``, and ``:``

    Args:
        text (str): text we are printing

    Return:
        None

    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    print_str = ""
    for i in text:
        if i is "." or i is "?" or i is ":":
            print_str += i
            print(print_str.strip(" ") + '\n')
            print_str = ""
        else:
            print_str += i
    print(print_str.strip(" "), end="")
