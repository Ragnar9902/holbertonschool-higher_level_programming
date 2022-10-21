#!/usr/bin/python3
"""Modulo almost a circle
python oriented programming
"""


class Base:
    """base class of the proyect
    """
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id == None:
            self.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
