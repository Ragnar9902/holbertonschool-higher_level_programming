#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

rectangle1 = Rectangle(3, 8)
print(rectangle1)
print(rectangle1.area())
