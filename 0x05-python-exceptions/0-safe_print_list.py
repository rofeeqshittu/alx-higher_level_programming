#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for item in range(x):
            print(my_list[item], end='')
            num += 1
        print()
    except (IndexError, ValueError):
        print()
        return num

    return num
