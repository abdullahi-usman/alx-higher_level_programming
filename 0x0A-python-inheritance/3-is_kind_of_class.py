#!/usr/bin/python3

'''
This Module test to see if there is
a correlation between these two
and tries to establish the relationship
'''


def is_kind_of_class(obj, a_class):
    '''
    Test if it is a subclass
    '''
    return issubclass(type(obj), a_class)
