#!/usr/bin/python3


def print_last_digit(number):
    str_num = str(number)
    str_num = str_num[len(str_num) - 1]
    print(str_num, end="")

    return int(str_num)
