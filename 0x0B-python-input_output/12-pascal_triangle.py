#!/usr/bin/python3
'''
This file has some
function that prints pascal triangle
and exit
'''


def factorial(n):
    '''
    factorial
    factorial
    factorial
    '''
    if n == 1:
        return n
    else:
        return n*factorial(n-1)


def pascal_triangle(n):
    '''
    Print pascal triangle
    Print pascal triangle
    Print pascal triangle
    Print pascal triangle
    '''

    list = []
    if n <= 0:
        return list

    for i in range(n):
        for j in range(i+1):
            list.append(factorial(i)//(factorial(j)*factorial(i-j)))

    return list
