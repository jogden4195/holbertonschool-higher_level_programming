#!/usr/bin/python3
i = '0'

while (ord(i) - 48) <= 99:
    print(str(ord(i) - 48) + ' = ' + str(hex(ord(i) - 48)))
    i = chr(ord(i) + 1)
