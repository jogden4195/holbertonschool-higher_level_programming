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
        self.__width = size

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, size):
        """ height - sets the height of the rectangle """
        self.__height = size

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, coord):
        """ x - sets the x coord. of the rectangle """
        self.__x = coord

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, coord):
        """ y - sets the y coord of the rectangle """
        self.__y = coord
