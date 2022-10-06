#!/usr/bin/python3
"""Tests driven developent
"""


def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    for row in matrix:
        for i in row:
            if type(i) is not float and type(i) is not int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return matrix