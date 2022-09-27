#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None) or (a_dictionary == {}):
        return None
    max_int = -1 * 10000000000000000000000000
    for i in a_dictionary:
        if max_int < a_dictionary[i]:
            max_int = a_dictionary[i]
            label_max = i
    return label_max
