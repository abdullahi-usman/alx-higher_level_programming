#!/usr/bin/python3
"""Module documentation of this said class
   And its infamous glory and all.
   This is going to be a new start
"""


class Rectangle:
    """Rectangle is a new class
    meant to calculate the area of
    rectangle and all that"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if type(w) != int:
            raise TypeError("width must be an integer")

        if w < 0:
            raise ValueError("width must be >= 0")

        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if type(h) != int:
            raise TypeError("height must be an integer")

        if h < 0:
            raise ValueError("height must be >= 0")

        self.__height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        if self.width == 0 or self.height == 0:
            return ""

        return (("#" * self.width + "\n") * self.height)[:-1]
