#!/usr/bin/python3
"""Rotate a matrix."""


def rotate_2d_matrix(matrix):
    """
    Rotate a matrix.

    args:
        matrix: a list of lists
    """
    n = len(matrix) - 1
    matrix_cp = []
    for i in range(n + 1):
        num_list = []
        for j in range(n, -1, -1):
            num_list.append(matrix[j][i])
        matrix_cp.append(num_list)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = matrix_cp[i][j]
