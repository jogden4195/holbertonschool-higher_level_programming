#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(list_a) < 2:
        if len(list_a) == 1:
            list_a.append(0)
        else:
            list_a.extend([0, 0])
    if len(list_b) < 2:
        if len(list_b) == 1:
            list_b.append(0)
        else:
            list_b.extend([0, 0])
    sum_a = list_a[0] + list_b[0]
    sum_b = list_a[1] + list_b[1]
    return (sum_a, sum_b)
