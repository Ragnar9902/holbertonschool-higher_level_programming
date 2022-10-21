#!/usr/bin/python3
"""Module almos a circle
"""

from models.base import Base


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
        """initializate function

        Args:
            width (int): descript one dimention of the rentangle__
            height (int): _descript one dimention of the rentangle_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """_summary_

        Returns:
            _int_: _description_
        """
        return self.width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self___width = value

    @height.setter
    def height(self, value):
        self___width = value

    @width.setter
    def x(self, value):
        self___x = value

    @height.setter
    def y(self, value):
        self.__y = value
