#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    c = 0
    try:
        for item in my_list[:x]:
            print("{:d}".format(item), end="")

        c = c + 1
    except Exception:
        pass

    print("")
    return c
