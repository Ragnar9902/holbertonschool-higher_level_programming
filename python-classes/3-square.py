#!/usr/bin/python3
"""Python classes
    this module is aid to practice the basis
    of python clases
"""


class Square():
    """This is a geometric figure
    of four sides
    """
    def __init__(self, size=0) -> None:
        """Initialization of the class square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        return (self.__size ^ 2)
