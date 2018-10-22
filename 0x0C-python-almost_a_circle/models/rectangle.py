#!/usr/bin/python3
""" Module for Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class - class for rectangles"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ - initializes a rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
        row = (' ' * self.__x) + ('#' * self.__width) + '\n'
        print(('\n' * self.__y) + (row * self.__height), end="")

    def __str__(self):
        """ __str__ - returns a informal description of the class """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ update - assigns an argument an argument to each attr """
        if args is not ():
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                    i += 1
                elif i == 1:
                    self.__width = arg
                    i += 1
                elif i == 2:
                    self.__height = arg
                    i += 1
                elif i == 3:
                    self.__x = arg
                    i += 1
                elif i == 4:
                    self.__y = arg
                    i += 1
        elif kwargs is not {}:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """ to_dictionary - returns the dict rep of rectangle """
        rec_dict = {}
        rec_dict['id'] = self.id
        rec_dict['width'] = self.__width
        rec_dict['height'] = self.__height
        rec_dict['x'] = self.__x
        rec_dict['y'] = self.__y
        return rec_dict
