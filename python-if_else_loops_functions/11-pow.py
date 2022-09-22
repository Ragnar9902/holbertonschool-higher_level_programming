#!/usr/bin/python3
def pow(a, b):
    if b > 0:
        temp = a
        for i in range(0, b - 1):
            temp = temp * a
    elif b < 0:
        temp = 1 / a
        for i in range(0, -1 * b - 1):
            temp = temp / a
    else:
        temp = 0
    return temp
