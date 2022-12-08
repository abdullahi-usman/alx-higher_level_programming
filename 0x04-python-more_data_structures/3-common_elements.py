#!/usr/bin/python3

def common_elements(set_1, set_2):

    common_it = []
    for name in set_1:
        if name in set_2:
            common_it.append(name)
    return (common_it)
