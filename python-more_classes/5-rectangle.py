#!/usr/bin/python3
"""Module 1-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """this function return a nice reprecentation of a rectangle
        """
        if self.height == 0 or self.width == 0:
            return ''
        Rect = ''
        for i in range(0, self.height):
            for j in range(0, self.width):
                Rect += '#'
            Rect += '\n'
        return Rect[:-1]

    def __repr__(self):
        """
        create a string representation of the Reactangle for val() use
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * self.width)

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (2 * self.height + 2 * self.width)
