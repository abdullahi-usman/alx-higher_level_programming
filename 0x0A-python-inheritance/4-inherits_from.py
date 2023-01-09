#!/usr/bin/python3

'''
Test subclasses only and report back
'''


def inherits_from(obj, a_class):
    '''
    Tell me if am a subclass and nothing else
    '''
    return type(obj) is not a_class and issubclass(type(obj), a_class)
