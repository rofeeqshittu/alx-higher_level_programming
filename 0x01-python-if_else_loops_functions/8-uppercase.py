#!/usr/bin/python3
def uppercase(str):
    str = list(str)
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 123:
            str[i] = chr(ord(str[i]) - ord('a') + ord('A'))
        else:
            str[i] = str[i]
    str = "".join(i for i in str)
    print("{}".format(str))
