#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":

    if len(argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    valid = ["+", "-", "*", "/"]

    if op not in valid:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif op == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif op == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif op == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif op == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
