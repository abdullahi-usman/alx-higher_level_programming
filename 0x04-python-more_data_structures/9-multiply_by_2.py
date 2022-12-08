#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = {}
    for mem in a_dictionary:
        new_dict[mem] = a_dictionary[mem] * 2
    return (new_dict)
