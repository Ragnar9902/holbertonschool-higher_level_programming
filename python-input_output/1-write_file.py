#!/usr/bin/python3
"""Module 3-write_file.
Writes in a text file.
"""


def write_file(filename="", text=""):
    """Writes text in filename.
    """

    with open(filename, 'w+') as f:
        return f.write(text)
