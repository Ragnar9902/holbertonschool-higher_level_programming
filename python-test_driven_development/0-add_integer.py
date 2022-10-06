#!/usr/bin/python3
"""Test driven developent
"""


def add_integer(a, b):
    """add two number if type integer or float
    """
    if not( isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not( isinstance(b, int) or isinstance(b, float)):    
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        result = int(a) + int(b)

    result = a + b

    if result == float('inf') or result == -float('inf'):
        return 89
