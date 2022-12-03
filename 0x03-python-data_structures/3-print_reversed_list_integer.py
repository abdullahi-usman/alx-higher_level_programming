#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print in reverse order

    Args:
        my_list: the list

    Returns:
        None
    """

    for item in reversed(my_list):
        print(item)
