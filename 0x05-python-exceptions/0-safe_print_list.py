#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    file_r = ""
    i = 0
    try:
        for item in my_list[:x]:
            file_r += "{:d}".format(item)
            i += 1
    except Exception:
        pass

    print(file_r)
    return i
