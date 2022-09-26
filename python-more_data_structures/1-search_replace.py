#!/usr/bin/python3
from operator import index


def search_replace(my_list, search, replace):
    new_list = []
    for index, element in enumerate(my_list):
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[index])
    return new_list
