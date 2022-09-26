#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for l, i in enumerate(my_list):
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[l])
    return new_list
 
