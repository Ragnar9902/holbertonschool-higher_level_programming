#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        None
    max = -1 * 100000000000000
    for k, i in enumerate(my_list):
        if i > max:
            max = i
    return max
