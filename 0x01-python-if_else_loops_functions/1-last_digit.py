#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = int(str(number)[-1])

# str_to_print = "Last digit of {:d} is {:d} ".format(number, last_digit)

if last_digit > 5:
    end = "is greater than 5"
elif last_digit == 0:
    end = "is 0"
else:
    end = "is less than 6 and not 0"

print("Last digit of {:d} is {:d} and {}".format(number, last_digit, end))
