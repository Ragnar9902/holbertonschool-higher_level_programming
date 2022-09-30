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
            raise TypeError        
        elif size < 0:
                raise ValueError
        self.__size = size
