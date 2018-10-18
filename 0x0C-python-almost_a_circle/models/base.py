#!/usr/bin/python3

class Base:
    """ Base class - base of all other classes """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """ __init__ - initializes the base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
