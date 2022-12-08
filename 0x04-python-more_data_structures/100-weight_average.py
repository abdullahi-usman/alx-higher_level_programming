#!/usr/bin/python3

def weight_average(my_list=[]):

    numeri = 0
    denomi = 0

    if len(my_list) == 0:
        return 0

    for num in list(map(lambda tp: tp[0] * tp[1], my_list)):
        numeri += num
    
    for num in my_list:
        denomi += num[1]
    
    return (numeri / denomi)
 