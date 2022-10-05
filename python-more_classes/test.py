#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = repr(my_rectangle)
print(new_rectangle)
print("--")
print(new_rectangle)
print("--")

print(type(new_rectangle) is type(my_rectangle))

del my_rectangle