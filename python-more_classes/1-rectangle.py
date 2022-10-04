#!/usr/bin/python3
"""Python clases
    in this module we explore some acvance feature of python OOP
"""


class Rectangle:
    """
    >>> my_rectangle = Rectangle(2, 4)
    >>> print(my_rectangle.__dict__)
    {'_Rectangle__height': 4, '_Rectangle__width': 2}
    >>> my_rectangle.width = 10
    >>> my_rectangle.height = 3
    >>> print(my_rectangle.__dict__)
    {'_Rectangle__height': 3, '_Rectangle__width': 10}
    """
    def __init__(self, width=0, height=0) -> None:

        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
