#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = int(str(number)[-1])
if number < 0:
    last_digit = last_digit * -1

str_to_print = "Last digit of {:d} is {:d} ".format(number, last_digit)

if last_digit > 5:
    str_to_print += "and is greater than 5"
elif last_digit == 0:
    str_to_print += "and is 0"
else:
    str_to_print += "and is less than 6 and not 0"

print("{}".format(str_to_print))
