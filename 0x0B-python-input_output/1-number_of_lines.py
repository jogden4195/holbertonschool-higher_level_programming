#!/usr/bin/python3
""" Module that returns number of lines """


def number_of_lines(filename=""):
    """ number_of_lines - returns number of lines in .txt """
    line_count = 0
    with open(filename, encoding='utf-8') as a_file:
        for i in a_file:
            line_count += 1
    return line_count
