#!/usr/bin/python3
"""Obtain minimum number of operations."""


def minOperations(n):
    """
    Get minimum amount of opration to complete a task.

    In our case, there is a single character `H` in a text file
    and we can only execute two operations, Copy All and Paste
    we want to obtain the minimum no. of operation to get exactly
    `n` character in a file.

    First, if `n` is one, we don't need to do anything
    as there is already one character in the file

    First, we create an array of n + 1 length that we'll
    hold the minimum no. of operations from 0 characters to `n`.

    In the outer loop, we set the elements in the loop
    with the worst-case number of operations
    i.e Copy ALL + (Paste + n - 1)
    which results to `n` operations.

    In the inner loop we then try to find optimal ways
    to reach to a specified `n` number of characters,
    if an optimal way is found, we update the array,
    if not the minimum number was already achieved.

    args:
        n (int): number of `H` characters need
    returns:
        the minimum number of operations needed
        to obtain `n` characters

    """
    if n == 1 or n < 0:
        return 0
    min_ops_arr = [0] * (n + 1)
    for i in range(2, n + 1):
        min_ops_arr[i] = i
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                min_ops_arr[i] = min_ops_arr[j] + (i // j)
                break
    return min_ops_arr[n]
