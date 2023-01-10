#!/usr/bin/python3
'''
Module to print
'''


def read_file(filename=""):
    '''
    Read the file and print it output
    '''
    with open(filename, encoding="utf-8") as file:
        print(file.read())
