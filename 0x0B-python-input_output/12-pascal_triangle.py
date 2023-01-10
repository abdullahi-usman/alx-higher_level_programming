#!/usr/bin/python3
'''
This file has some
function that prints pascal triangle
and exit
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
