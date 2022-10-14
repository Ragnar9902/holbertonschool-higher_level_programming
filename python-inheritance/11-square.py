#!/usr/bin/python3
"""Module 10-square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits and extends the properties of Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self) -> str:
        return str("[Square] {}/{}".format(self.__size, self.__size))
