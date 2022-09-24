#!/usr/bin/python3
def no_c(my_string):
    count = 0
    for i in my_string:
        if i == 'c' or i == 'C':
            my_string[count] = ''
        count += 1
    return my_string
