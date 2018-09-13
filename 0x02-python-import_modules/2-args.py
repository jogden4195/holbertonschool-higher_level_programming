#!/usr/bin/python3
import sys

print("{:d} arguments".format(len(sys.argv[1:])), end="")
if (len(sys.argv[1:])) == 0:
    print(".")
else:
    print(":")
    for i in sys.argv[1:]:
        print("{:d}: {}".format(sys.argv.index(i), i))
