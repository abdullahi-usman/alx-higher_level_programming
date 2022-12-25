#!/usr/bin/python3
"""matrix division, this is very intersting
first we make sure it a matrix of valid size,
and that all items are integers or floats
and also the divisor is a valid integer input
so lets begin
"""


def matrix_divided(matrix, div):

    """ This is very nice, make sure we have
    a new matrix, that we will transfer back,
    then check everything
    """
    new_matrix = []
    if (type(matrix) != list or not
        all([True for line in matrix for item in line
            if type(item) in [int, float]])):

        raise TypeError("matrix must be a matrix \
            (list of lists) of integers/floats")

    all_items = [len(line) for line in matrix]

    if (max(all_items) != min(all_items)):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if (div == 0):
        ZeroDivisionError("division by zero")

    for line in matrix:
        new_matrix.append([round(float(f"{item / div}"), 2) for item in line])

    return new_matrix
