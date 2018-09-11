def print_last_digit(number):
    if number >= 0:
        number = number % 10
    else:
        number = number % -10
        number = -(number)
    print("{:d}".format(number), end="")
    return (number)
