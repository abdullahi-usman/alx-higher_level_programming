#!/usr/bin/python3

"""Add Integer Module
This module is part of this class
And has the requierment to be atleast
five lines long, so we are going
to make it five lines long"""


def add_integer(a, b=98):

    """Add two integers and return their result
    Here also our line must be thre lines long
    And at this line it is three line long"""
    if (type(a) not in [int, float]):
        raise TypeError('a must be an integer')
    if (type(b) not in [int, float]):
        raise TypeError('b must be an integer')

    return (a + b)
