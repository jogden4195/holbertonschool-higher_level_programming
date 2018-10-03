#!/usr/bin/python3
class Square:
    """Square - defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ __init__ - initializes the object

        Attributes:
            size (int): size of the square
            position (tuple): positions the square

        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        if type(position) is tuple:
            for i in position:
                if type(i) is not int or i < 0:
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
            if len(position) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            self.__position = position

    @property
    def size(self):
        """ size - gets the size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ position - coordinates for where we want our square """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple:
            for i in value:
                if type(i) is not int or i < 0:
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
            if len(value) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """ area - returns the current square area"""
        return self.__size**2

    def my_print(self):
        """ my_print - prints in stdout the square with the character '#' """
        row = ""
        row += (" " * self.position[0]) + ("#" * self.__size)
        print("\n" * self.position[1], end="")
        for i in range(self.__size):
            print(row)
