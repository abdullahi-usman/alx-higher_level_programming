#!/usr/bin/python3


def print_last_digit(number):
    str_num = str(number)
    return (int((str_num[str_num[len(str_num) -1] if len(str_num) > 1  else 0])))