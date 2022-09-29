#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div_s = False
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            div_s = True
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except TypeError:
            div = 0
            print("wrong type")
        except IndexError:
            print("out of range")
            div = 0
        finally:
            if div_s:
                new_list.append(div)
            else:
                new_list.append(0)
    return new_list
