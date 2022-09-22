#!/usr/bin/python3
for n in range(0, 100):
    if (n < 10):
        print("0{}, ".format(n), end="")
    elif (n != 99):
        print("{}, ".format(n, hex(n)), end="")
    else:
        print("99", end="")
