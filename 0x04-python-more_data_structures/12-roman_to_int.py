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
        while i < len(my_str) - 1:
            if i == 0:
                if values[my_str[0]] >= values[my_str[i + 1]]:
                    total += values[my_str[0]]
                else:
                    total -= values[my_str[0]]
                i += 1
            elif values[my_str[i]] >= values[my_str[i + 1]]:
                total += values[my_str[i]]
                i += 1
            else:
                while values[my_str[i]] <= values[my_str[i + 1]]:
                    total -= values[my_str[i]]
                    i += 1
    total += values[my_str[-1]]
    return total
