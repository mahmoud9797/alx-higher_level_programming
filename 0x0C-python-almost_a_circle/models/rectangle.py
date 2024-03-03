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
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        self.__width = value

    @property
    def height(self):
        """rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """x is rectangle coordinate"""
        self.__x = value

    @property
    def y(self):
        """y is the rectangle coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        self.__y = value
