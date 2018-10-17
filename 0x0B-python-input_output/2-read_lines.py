#!/usr/bin/python3
""" Module that reads n lines of a .txt """


def read_lines(filename="", nb_lines=0):
    """ read_lines - reads n lines of a text file & prints it """
    with open(filename, encoding='utf-8') as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
        else:
            j = 0
            for i in a_file:
                print(i.strip())
                j += 1
                if j == nb_lines:
                    break
