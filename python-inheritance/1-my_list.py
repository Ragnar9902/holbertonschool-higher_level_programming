#!/usr/bin/python3
"""Python inheritance
"""


class My_list(list):
    """extend the list class."""

    def print_sorted(self):
        """Prints the list, in ascending sort."""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
