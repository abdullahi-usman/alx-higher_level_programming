#!/usr/bin/python3
""" This module is made to say the name
of input and it contains only one
function and suppose to be atleast five
lines long, so may we are going to
stop here"""


def say_my_name(first_name, last_name=""):

    """ This function is going to print
    the name of the first and also the
    last name
    """
    if (type(first_name) != str):
        raise TypeError("first_name must be a string")

    if (type(last_name) != str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
