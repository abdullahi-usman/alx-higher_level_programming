#!/usr/bin/python3

'''
Rectangle Module of baseGeometry
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Rectangle MOdule derived fom base geometry
    '''

    def __init__(self, width, height):
        '''
        init function
        '''
        super().__init__()

        super().integer_validator('width', width)
        super().integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        '''
        Return the area of a rectangle
        '''
        return self.__height * self.__width

    def __str__(self):

        '''
        Return the string representation
        '''
        return f"[Rectangle]{self.__width}/{self.__height}"
