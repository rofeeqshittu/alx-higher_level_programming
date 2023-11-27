#!/bin/usr/python3
def print_reversed_list_integer(my_list=[]):
    for item in reversed(range(len(my_list))):
        print("{}".format(my_list[item]))
