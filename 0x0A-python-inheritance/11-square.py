#!/usr/bin/python3

'''
Rectangle Module of baseGeometry
'''

MSquare = __import__('10-square').Square


class Square(MSquare):
    '''
    Rectangle MOdule derived fom base geometry
    '''

    def __init__(self, size):
        '''
        init function
        '''
        super().__init__(size)