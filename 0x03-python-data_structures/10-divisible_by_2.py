#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or my_list == []:
        return None
    cool_beanz = []
    for i in my_list:
        if i % 2 == 0:
            cool_beanz.append(True)
        else:
            cool_beanz.append(False)
    return cool_beanz
