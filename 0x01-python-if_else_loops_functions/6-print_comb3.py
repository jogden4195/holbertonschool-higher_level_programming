#!/usr/bin/python3
for i in range(1, 100):
    if i < 10 or (int(str(i)[0]) < int(str(i)[-1])):
        if i < 89:
            print("{:02d},".format(i), end=" ")
        else:
            print("{:02d}".format(i))
