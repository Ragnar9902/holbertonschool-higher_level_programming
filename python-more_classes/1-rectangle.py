#!/usr/bin/python3
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

        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width must be an integer")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
