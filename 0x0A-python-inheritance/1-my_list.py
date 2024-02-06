#!/usr/bin/python3
""" mylist subclass """


class MyList(list):
    def __init__(self):
        """initaize object"""
        super().__init__()
    def print_sorted(self):
        print(sorted(self))
