def uppercase(str):
    for c in str:
        letter = ord(c)
        if (letter >= 97 and letter <= 122):
            letter -= 32
        letter = chr(letter)
        print("{}".format(letter), end="")
    print("")
