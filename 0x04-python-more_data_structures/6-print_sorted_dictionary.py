#!/usr/bin/python3

def m_compare(str):
    return (ord(str[0]))


def print_sorted_dictionary(a_dictionary):
    dict_keys = []
    for key in a_dictionary:
        dict_keys.append(key)

    dict_keys = sorted(dict_keys, key=m_compare)

    for key in dict_keys:
        print(f"{key}: {a_dictionary[key]}")
