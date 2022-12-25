#!/usr/bin/python3
"""This module is going to print a sqaure,
depending on the input. it is also going to check
for valid inputs. Only integers are allowed
so we are to watch ver very carefull
and very quite and much
"""


def print_square(size):

    """Check very very before trying to
    print and square. we make sure any other
    input are ignored.
    """
    if type(size) != int or (type(size) == float and size < 0.0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
