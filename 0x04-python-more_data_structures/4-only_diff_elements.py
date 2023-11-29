#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    n_set_1 = list(set_1)
    n_set_2 = list(set_2)

    for num1 in n_set_1[:]:
        for num2 in n_set_2[:]:
            if num1 == num2:
                n_set_1.remove(num1)
                n_set_2.remove(num2)

    uniq_elem = n_set_1[:] + n_set_2[:]
    return set(uniq_elem)
