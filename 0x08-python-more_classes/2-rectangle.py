#!/usr/bin/python3
class Rectangle:
    """ Rectangle - Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """ __init - initializes the rectangle

        Attributes:
            width: how wide the rectangle will be
            height: how tall the rectangle will be

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width - gets the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height - gets the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area - returns the current rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter - returns the current rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
