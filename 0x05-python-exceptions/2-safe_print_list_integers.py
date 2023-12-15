#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = uns = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[num]), end='')
            num += 1
            if num == x:
                print()
                return num
        except (ValueError, TypeError):
            num += 1
            uns += 1
    print()
    return num - uns
