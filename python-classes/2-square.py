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
            if size > 0:
                self.__size = size
            else:
                raise ValueError
        else:
            raise TypeError        
