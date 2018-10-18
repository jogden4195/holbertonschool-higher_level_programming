#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """ Rectangle class - class for rectangles"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ - initializes a rectangle """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

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
        return self.__height

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
        return self.__x

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

    def area(self):
        """ area - returns the area value of the Rectangle instance """
        return (self.__width * self.__height)

    def display(self):
        """ display - prints the rectangle with '#' characters """
        row = ('#' * self.__width) + '\n'
        print(row * self.__height, end="")

    def __str__(self):
        """ __str__ - returns a informal description of the class """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
