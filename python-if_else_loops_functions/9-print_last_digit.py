#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        ld = -1 * number
        ld = (ld % 10)
    else:
        ld = number % 10
    print("{}".format(ld), end="")
    return ld
