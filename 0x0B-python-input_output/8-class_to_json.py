#!/usr/bin/python3
'''
COntains python function that
return a object as a JSON
representation
'''


def class_to_json(obj):
    '''
    Return this object as JSON
    representation of all of
    its variables
    '''
    return vars(obj)
