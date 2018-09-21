#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if type(roman_string) is str and roman_string is not None:
        my_str = list(roman_string)
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        if len(my_str) == 1:
            return (values[my_str[i]])
        while i < len(my_str) - 1:
            current = values[my_str[i]]
            next_num = values[my_str[i + 1]]
            if current >= next_num:
                total += current
                i += 1
            else:
                total -= current
                i += 1
        total += values[my_str[-1]]
    return abs(total)
