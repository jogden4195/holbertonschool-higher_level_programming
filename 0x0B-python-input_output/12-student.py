#!/usr/bin/python3


class Student:
    """ Student - Defines a student """
    def __init__(self, first_name, last_name, age):
        """ __init__ - initializes a student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json - retrieves a dictionary rep of a Student """
        if attrs is not None:
            my_dict = {}
            for i in attrs:
                if i is "first_name":
                    my_dict[i] = self.first_name
                elif i is "last_name":
                    my_dict[i] = self.last_name
                elif i is "age":
                    my_dict[i] = self.age
                else:
                    pass
            return my_dict
        else:
            return self.__dict__
