#!/usr/bin/python3
from models.base import Base
""" First Rectangle """


class Rectangle(Base):
    """ creat Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initalize instance """
        super().__init__(id)
        """ inherit id fron Base class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area of rectangle """
        return self.width * self.height

    def display(self):
        """ print rectangle with x and coordinate """
        for n in range(self.y):
            print("")
        for r in range(self.height):
            print(" ", end="")
            print("#" * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".\
                format(self.id, self.x, self.y, self.width, self.height)