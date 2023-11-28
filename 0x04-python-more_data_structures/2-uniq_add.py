#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    uniq_set = list(uniq_set)
    sum = 0
    for i in range(len(uniq_set)):
        sum += uniq_set[i]
    return sum
