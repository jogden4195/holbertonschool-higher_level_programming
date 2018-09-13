#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        print("0 arguments.")
    else:
        if len(sys.argv[1:]) == 1:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(len(sys.argv[1:])))
        for i in sys.argv[1:]:
            print("{:d}: {}".format(sys.argv.index(i), str(i)))
