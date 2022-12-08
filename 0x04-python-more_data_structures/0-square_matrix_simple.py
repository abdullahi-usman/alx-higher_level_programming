#!/usr/bin/python3




def square_matrix_simple(matrix=[]):
    new_matrix = []
    for arr in matrix:
        n_arr = []
        for num in arr:
            n_arr.append(num * num)
        new_matrix.append(n_arr)
