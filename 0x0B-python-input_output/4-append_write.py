#!/usr/bin/python3
""" Module that appends a str to end of .txt """


def append_write(filename="", text=""):
    """ append_write - appends a str to the end of a text file """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        i = 0
        for char in text:
            a_file.write(char)
            i += 1
    return i
