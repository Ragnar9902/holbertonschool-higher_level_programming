def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx > (len(my_list) - 1) or idx < 0:
        return copy
    copy[idx] = element
    return copy
