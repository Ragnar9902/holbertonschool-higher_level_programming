#!/usr/bin/python3
"""Module 5-base_geometry
"""


class BaseGeometry:
    """Empty Class"""

    def area(self):
        """raise a error"""

        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        """Validates value."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
