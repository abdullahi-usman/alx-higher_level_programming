#!/usr/bin/python3
'''
Module to print input
and output of the file
'''


def read_file(filename=""):
    '''
    Read the file and print it output
    using utf-8 and make sure its close
    '''
    with open(filename, encoding="UTF8") as file:
        print(file.read())
