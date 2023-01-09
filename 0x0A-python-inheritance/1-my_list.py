#!/usr/bin/python3
'''
Inherit from the global list class
and print all that is it
'''


class MyList(list):

    '''
    Inherit me and print all my glory
    '''
    def print_sorted(self):
        print(sorted(self))
