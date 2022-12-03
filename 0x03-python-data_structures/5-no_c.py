#!/usr/bin/python3

def no_c(my_string):
    new_str = list(my_string)

    for index in range(0, len(new_str)):
        if new_str[index].upper() == 'C':
            new_str[index] = ''

    return str().join(new_str)
