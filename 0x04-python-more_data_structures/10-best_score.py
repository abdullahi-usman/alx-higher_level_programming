#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    
    res = 0
    for mem in a_dictionary:
        if a_dictionary[mem] > res:
            res = a_dictionary[mem]
    
    return (res if res != None else None)