#!/usr/bin/env python3
def uppercase(str):
    for c in str:
        letter = ord(c)
        if (letter >= 97 and letter <= 122):
            letter -= 32
        print("{}".format(chr(letter)), end="")
    print("")
