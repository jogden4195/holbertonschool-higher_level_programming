#!/usr/bin/python3
""" Module for pascal's triangle """


def pascal_triangle(n):
    triangle = []
    i = 1
    while i <= n:
        if i == 1:
            triangle.append([1])
            i += 1
        elif i == 2:
            triangle.append([1, 1])
            i += 1
        else:
            last = triangle[i - 2]
            new_row = []
            for j in range(i):
                new_row.append(1)
            k = 1
            while k < i - 1:
                new_row[k] = last[k] + last[k-1]
                k += 1
            triangle.append(new_row)
            i += 1
    return triangle
