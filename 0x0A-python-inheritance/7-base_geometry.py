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

    def integer_validator(self, name, value):
        if isinstance(type(value), int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
