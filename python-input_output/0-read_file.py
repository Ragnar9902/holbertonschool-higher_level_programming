#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""


def read_file(filename=""):
    """Reads from filename and prints
    its contents to stdout.
    """

    with open(filename) as fp:
        readed_text = fp.read()
        print(readed_text, end="")
