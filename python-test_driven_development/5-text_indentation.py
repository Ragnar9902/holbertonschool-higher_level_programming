#!/usr/bin/python3
"""test driven developent
"""


def text_indentation(text):
    """
    add format to a string to print
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
