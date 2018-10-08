#!/usr/bin/python3
class Rectangle:
    """ Rectangle - Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """ __init__ - initializes the rectangle

        Attributes:
            width: how wide the rectangle will be
            height: how tall the rectangle will be

        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def __str__(self):
        """ __str__ - prints a readable message """
        row = ""
        if self.__width != 0 and self.__height != 0:
            i = 1
            while i <= self.__height:
                row += "#" * self.__width
                if i is not self.__height:
                    row += "\n"
                i += 1
        return row

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
        return (2 * self.__width) + (2 * self.__height)
