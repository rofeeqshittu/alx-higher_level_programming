#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    for char in range(len(my_string)):
        if my_string[char] == 'c':
            del (new_string[char])
        elif my_string[char] == 'C':
            del (new_string[char])
    listToStr = "".join(str(elem) for elem in new_string)
    return listToStr
