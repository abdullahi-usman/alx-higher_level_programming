#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if (len(matrix) > 0 and len(matrix[0]) > 0):
        for arr in matrix:
            print("{} {} {}".format(arr[0], arr[1], arr[2]))
