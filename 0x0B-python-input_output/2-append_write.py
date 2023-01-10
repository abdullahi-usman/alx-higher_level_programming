#!/usr/bin/python3

'''
FIle for functions that write to
the end of the file and
return their written status
'''


def append_write(filename="", text=""):
    '''
    Write this text to the end of the file
    and return the number of charater
    written
    '''
    with open(filename, mode='a+') as file:
        return file.write(text)
