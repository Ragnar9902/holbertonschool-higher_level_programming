#!/usr/bin/python3
def roman_to_int(Roman_string):
    if not isinstance(Roman_string, str) or Roman_string is None:
        return 0
    r_numbers = {"L": 50, "V": 5, "X": 10, "C": 100, "D": 500, "I": 1}
    R_number = 0
    for iter, i in enumerate(Roman_string):
        if iter > 0 and r_numbers[i] > r_numbers[Roman_string[iter - 1]]:
            R_number += r_numbers[i] - 2 * r_numbers[Roman_string[iter - 1]]
        else:
            R_number += r_numbers[i]
    return R_number
