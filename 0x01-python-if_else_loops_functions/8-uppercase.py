#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 122 >= ord(c) >= 97:
            result += chr(ord(c) - 32)
    print("{}".format(result))
