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

    def area(self):
        """ area - returns the area of the rectangle """
        return self.__height * self.__width

    def __str__(self):
        """ __str__ - returns an informal print statement """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """ Square - Defines a square """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area - returns the area of the square """
        return self.__size ** 2

    def __str__(self):
        """ __str__ - returns an informal print statement """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
