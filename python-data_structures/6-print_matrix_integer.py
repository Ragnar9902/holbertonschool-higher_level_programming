#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        return print("")
    for i in matrix:
        for k, j in enumerate(i):
            if k == len(i) - 1:
                print("{:d}".format(j))
                continue                
            print("{:d}".format(j), end=" ")
