#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda arr: [arr[0] * arr[0],
                arr[1] * arr[1], arr[2] * arr[2]], matrix))
