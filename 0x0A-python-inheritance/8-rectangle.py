#!/usr/bin/python3


class BaseGeometry:
    """ BaseGeometry - Defines a Based Shape """

    def area(self):
        """ area - raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator - validates a value

        Arguments:
            name (str): name
            value (int): value

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle - Defines a Rectangle """

    def __init__(self, width, height):
        """ __init__ - initializes the rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
