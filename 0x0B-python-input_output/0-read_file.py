#!/usr/bin/python3
""" module to read text file"""


def read_file(filename=""):
    """ function take txt filename --->
    open it ---> read it ---> print it --->"""
    with open(filename, encoding="utf-8") as txt_f:
        print(txt_f.read(), end="")
