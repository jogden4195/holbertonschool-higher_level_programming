#!/usr/bin/python3
""" Module to write a string to a .txt """


def write_file(filename="", text=""):
    """ write_file - writes a string to a text file """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        i = 0
        for char in text:
            a_file.write(char)
            i += 1
    return i
