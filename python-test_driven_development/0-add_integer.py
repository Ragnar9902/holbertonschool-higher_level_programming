#!/usr/bin/python3
"""Test driven developent
"""


def add_integer(a, b):
    """add two number if type integer or float
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):    
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        return int(a) + int(b)

    return a + b
