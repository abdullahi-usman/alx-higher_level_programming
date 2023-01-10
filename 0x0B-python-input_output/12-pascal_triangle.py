#!/usr/bin/python3
'''
Has student information to print
and store some information
in a file
'''

from math import factorial


def pascal_triangle(n):
    '''
    Print pascal triangle
    '''
    for i in range(n):
        print('[', end='')
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end="")

            if j != i:
                print(',', end='')

        print(']')
