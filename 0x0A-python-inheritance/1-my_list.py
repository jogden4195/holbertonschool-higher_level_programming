#!/usr/bin/python3
""" Module for MyList class """


class MyList(list):
    """ MyList - defines a list 

    Modules:
        print_sorted: prints the list

    """
    def __init__(self):
        """ __init__ - initializes MyList """
        super().__init__(self)

    def print_sorted(self):
        """ print_sorted - prints the list """
        print(sorted(self))
