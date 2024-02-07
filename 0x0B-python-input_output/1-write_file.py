#!/usr/bin/python3
""" function used to write on text file"""


def write_file(filename="", text=""):
    """two args :
    filename ( is the name of text file we will write on it
    text is the text we would like to write it on the file"""

    with open(filename, "w", encoding="utf-8") as txt_f:
        return txt_f.write(text)
