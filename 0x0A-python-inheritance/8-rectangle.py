#!/usr/bin/python3

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle - Defines a Rectangle """

    def __init__(self, width, height):
        """ __init__ - initializes the rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
