#!/usr/bin/python3
'''
This file has write functions
to write to a file
'''


def write_file(filename="", text=""):
    '''
    Write this text to the file
    '''
    with open(filename, mode='w+', encoding='utf-8') as file:
        return file.write(text)
