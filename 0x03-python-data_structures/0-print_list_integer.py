#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """print this list

    Args:
        my_list: the list

    Returns:
        None
    """
    
    for num in my_list:
        print("{:d}".format(num))
