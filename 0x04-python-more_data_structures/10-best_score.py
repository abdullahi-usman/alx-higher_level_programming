#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)

    res = None
    re_int = 0
    for mem in a_dictionary:
        if a_dictionary[mem] is not None and a_dictionary[mem] > re_int:
            res = mem
            re_int = a_dictionary[mem]

    return (res if res is not None else None)
