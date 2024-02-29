#!/usr/bin/python3
"""rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle calss inherint"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """rectangle width"""
        return self.width

    @width.setter
    def width(self, value):
        """ width setter """
        self.width = value

    @property
    def height(self):
        """rectangle height"""
        return self.height

    @height.setter
    def height(self, value):
        self.height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        """x is rectangle coordinate"""
        self.x = value

    @property
    def y(self):
        """y is the rectangle coordinate"""
        return self.y
    
    @y.setter
    def y(self, value):
        """ y setter """
        self.y = value
