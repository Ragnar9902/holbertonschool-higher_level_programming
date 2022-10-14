#!/usr/bin/python3
"""Module 2-is_same_class.
"""


def is_same_class(obj, a_class):
    """determinated whether an object is istance of a class"""
    if type(obj) == a_class:
        return True
    else:
        return False
