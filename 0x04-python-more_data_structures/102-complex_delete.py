#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for name in new_dict.keys():
        if a_dictionary[name] == value:
            del (a_dictionary[name])

    return (a_dictionary.copy())
