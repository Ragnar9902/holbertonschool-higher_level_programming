#!/usr/bin/python3
"""Python classes
    this module is aid to practice the basis
    of python clases
"""


class Square():
    """This is a geometric figure
    of four sides
    """
    def __init__(self, size=0):
        """Initialization of the class square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """Return the area of the square"""
        return ((self.__size) ** 2)


my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))