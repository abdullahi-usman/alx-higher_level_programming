#!/usr/bin/python3

'''
Base Geometry class
and evil one
'''


class BaseGeometry:
    '''
    Base class geometry
    '''

    def area(self):
        '''
        Raises an exception letting us know that
        it is not implemented
        '''
        raise Exception('area() is not implemented')
