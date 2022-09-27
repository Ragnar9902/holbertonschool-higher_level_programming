#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("{:d}".format(result))
        return result
    except:
        pass
