#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    if n > len(str):
        return str
    new_str = list(str[:])
    del (new_str[n])
    new_str = "".join(i for i in new_str)
    return new_str
