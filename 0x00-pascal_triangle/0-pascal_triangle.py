#!/usr/bin/python3
"""Pascal's triangle module."""


def pascal_triangle(n):
    """Return a matrix representing pascal's triangle."""
    matrix = []

    for i in range(n):
        row = []

        row.append(1)
        if i > 0:
            for j in range(i - 1):
                row.append(matrix[i - 1][j] + matrix[i - 1][j + 1])
            row.append(1)
        matrix.append(row)
    return matrix
