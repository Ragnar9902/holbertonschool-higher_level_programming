from cProfile import label


def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    max_int = -1 * 1000000000000000000000000
    for i in a_dictionary:
        if max_int < a_dictionary[i]:
            max_int = a_dictionary[i]
            label_max = i
    return label_max

