#!/usr/bin/python3
for n in range(0, 99):
    if (n < 10):
        print("0{}, ".format(n), end="")
    elif (n != 98):
        print("{}, ".format(n, hex(n)), end="")
    else:
        print("98", end="")
