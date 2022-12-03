#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (len(matrix) > 0):
        for arr in matrix:
            if (len(arr) == 3):
                print("{:d} {:d} {:d}".format(arr[0], arr[1], arr[2]))
