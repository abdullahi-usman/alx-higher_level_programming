#!/usr/bin/python3
'''
Module to print input
and output of the file
'''


from asyncore import read


def read_file(filename=""):
    '''
    Read the file and print it output
    using utf-8 and make sure its close
    '''
    with open(filename, encoding="utf-8") as file:
        print(file.read())
