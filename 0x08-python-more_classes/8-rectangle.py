#!/usr/bin/python3
"""Module documentation of this said class
   And its infamous glory and all.
   This is going to be a new start
"""


class Rectangle:
    """Rectangle is a new class
    meant to calculate the area of
    rectangle and all that"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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

        sym = f"{self.print_symbol}"
        return ((sym * self.width + "\n") * self.height)[:-1]

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_2 if rect_2.area() > rect_1.area() else rect_1
