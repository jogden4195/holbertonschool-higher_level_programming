#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ matrix_divided - divides all elements of a matrix

    Args:
        matrix (list): list of lists of integers or floats
        div (int or float): number we are dividing matrix by

    Returns:
        new matrix of divided values

    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if matrix == [[]] or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix[0])
    for x in matrix:
        if type(x) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        new_row_len = len(x)
        if new_row_len != row_len:
            raise TypeError(
                "Each row of the matrix must have the same size")
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats")
    return [[round(y / div, 2) for y in x] for x in matrix]
