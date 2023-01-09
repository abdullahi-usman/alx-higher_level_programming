#!/usr/bin/python3

'''
Rectangle Module of baseGeometry
'''

BaseGeometry = __import__('8-rectangle').Rectangle


class Rectangle(BaseGeometry):
    '''
    Rectangle MOdule derived fom base geometry
    '''

    def __init__(self, width, height):
        '''
        init function
        '''
        super().__init__(width, height)

    def area(self):
        '''
        Return the area of a rectangle
        '''
        return self.__height * self.__width

    def __str__(self):

        '''
        Return the string representation
        '''
        return f"[{type(self).__name__}]{self.__width}/{self.__height}"
