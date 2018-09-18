#!/usr/bin/python3
def no_c(my_string):
    my_string_list = list(my_string)
    for i in my_string_list:
        if i == "c" or i == "C":
            my_string_list.remove(i)
    return ''.join(my_string_list)
