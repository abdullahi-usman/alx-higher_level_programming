#!/usr/bin/python3

def uniq_add(my_list=[]):
    add_list = []
    res = 0
    for num in my_list:
        if num not in add_list:
            add_list.append(num)
            res += num
    return (res)
