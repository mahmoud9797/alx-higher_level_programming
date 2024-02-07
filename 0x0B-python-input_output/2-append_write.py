#!/usr/bin/python3
"""function to append text to text file"""


def append_write(filename="", text=""):
    """args: filename and text will be added"""

    with open(filename, "a", encoding="utf-8") as txt_f:
        return txt_f.write(text)
