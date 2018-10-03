#!/usr/bin/python3
class Square:
    """Square - defines a square"""
    def __init__(self, size=0):
        """ __init__ - initializes the object

        Attributes:
            size (int): size of the square

        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ area - returns the current square area"""
        return self.__size**2
