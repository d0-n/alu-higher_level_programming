#!/usr/bin/python3


def uppercase(str):
    result = ""
    for i in range(len(str)):
        c = str[i]
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            result = result + chr(ord(c) - 32)
        else:
            result = result + c
    print("{}".format(result))
