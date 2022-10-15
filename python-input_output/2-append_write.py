#!/usr/bin/python3
"""Module 2-apped_write.
Writes in the end text file.
"""


def write_file(filename="", text=""):
    """add text in the end of the file filename.
    """

    with open(filename, 'a') as f:
        return f.write(text)
