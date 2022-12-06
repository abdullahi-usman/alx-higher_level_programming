#!/usr/bin/python3

def uppercase(str):
    print("{}".format(''.join([chr((ord(c) - 32)) for c in str])))