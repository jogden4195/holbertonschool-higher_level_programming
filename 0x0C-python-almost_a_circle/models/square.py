#!/user/bin/python
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class - a subclass of the rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ __init__ - initializes the square """
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y
        self.__id = id
        
    def __str__(self):
        """ __str__ - prints a informal description of a square instance """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.__x, self.__y, self.__width)
