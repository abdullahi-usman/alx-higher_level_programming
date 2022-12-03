#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []

    for item in my_list:
        new_list.append(False if item % 2 else True)

    return (new_list)
