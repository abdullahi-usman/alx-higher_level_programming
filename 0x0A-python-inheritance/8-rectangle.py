#!/usr/bin/python3

'''
Rectangle Module of baseGeometry
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
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
