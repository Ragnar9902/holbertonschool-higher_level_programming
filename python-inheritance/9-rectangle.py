#!/usr/bin/python3
"""Module 5-base_geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits and extends the properties of basegeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        super().__init__()

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self) -> str:
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
