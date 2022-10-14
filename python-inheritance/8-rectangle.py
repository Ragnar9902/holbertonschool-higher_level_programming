#!/usr/bin/python3
"""Module 5-base_geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits and extends the properties of basegeometry"""

    def __init__(self, width, height):
        super().__init__()
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("width must be greater than 0")
        if height <= 0:
            raise ValueError("width must be greater than 0")

        self.__width = width
        self.__height = height
