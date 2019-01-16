#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    find_peak - finds a peak in a list of unsorted integers
    Return: peak of the list
    """
    if list_of_integers != []:
        sorted_list = list_of_integers.sort()
        return sorted_list[-1]
    return None
