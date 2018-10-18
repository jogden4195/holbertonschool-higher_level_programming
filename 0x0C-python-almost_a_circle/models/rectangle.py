#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """ Rectangle class - class for rectangles"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ - initializes a rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, size):
        """ width - sets the width of the rectangle """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = size

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, size):
        """ height - sets the height of the rectangle """
        if type(size) is not int:
            raise TypeError("height must be an integer")
        if size <= 0:
            raise ValueError("height must be > 0")
        self.__height = size

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, coord):
        """ x - sets the x coord. of the rectangle """
        if type(coord) is not int:
            raise TypeError("x must be an integer")
        if coord < 0:
            raise ValueError("x must be >= 0")
        self.__x = coord

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, coord):
        """ y - sets the y coord of the rectangle """
        if type(coord) is not int:
            raise TypeError("y must be an integer")
        if coord < 0:
            raise ValueError("y must be >=0")
        self.__y = coord
