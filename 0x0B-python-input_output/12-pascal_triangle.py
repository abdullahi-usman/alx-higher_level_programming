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
    if n <= 1:
        return 1
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



def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))


