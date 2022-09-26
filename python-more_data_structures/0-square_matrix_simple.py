#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squart_M = matrix.copy()
    for l, i in enumerate(squart_M):
        for k, j in enumerate(i):
            squart_M[l][k] = j*j
    return squart_M
