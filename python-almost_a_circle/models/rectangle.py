#!/usr/bin/python3
"""Module almos a circle
"""

Base = __import__('base').Base
class Rectangle(Base):
    """class that represent a rectangle

    Args:
        Base (_type_): _description_
        Private instance attribute: width
        Private instance attribute: height
        Private instance attribute: x
        Private instance attribute: y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        self___width = value

    @height.setter
    def height(self, value):
        self___width = value
