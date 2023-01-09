#!/usr/bin/python3

'''
Rectangle Module of baseGeometry
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Rectangle MOdule derived fom base geometry
    '''

    def __init__(self, size):
        '''
        init function
        '''
        super().__init__(size, size)