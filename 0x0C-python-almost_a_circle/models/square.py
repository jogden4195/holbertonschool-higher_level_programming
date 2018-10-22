#!/user/bin/python3
""" Module for Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class - a subclass of the rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ __init__ - initializes the square """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """ size - sets the value for size """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ __str__ - prints a informal description of a square instance """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ update - updates attributes """
        if args is not ():
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                    i += 1
                elif i == 1:
                    self.size = arg
                    i += 1
                elif i == 2:
                    self.x = arg
                    i += 1
                elif i == 3:
                    self.y = arg
                    i += 1
        elif kwargs is not {}:
            for arg in kwargs:
                if arg == "id":
                    self.id = kwargs.get(arg)
                elif arg == "size":
                    self.size = kwargs.get(arg)
                elif arg == "x":
                    self.x = kwargs.get(arg)
                elif arg == "y":
                    self.y = kwargs.get(arg)

    def to_dictionary(self):
        """ to_dictionary - returns the dict rep of a Square """
        sq_dict = {}
        sq_dict['id'] = self.id
        sq_dict['size'] = self.size
        sq_dict['x'] = self.x
        sq_dict['y'] = self.y
        return sq_dict
