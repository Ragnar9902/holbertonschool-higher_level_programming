#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("{:d}".format(result))
    except:
        return None
    finally:
        print("Inside result: {:d}".format(result))
        return result