#!/usr/bin/python3
"""Place n non-attacking queens on a n * n chessboard."""

from sys import argv, exit
from typing import List


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    n = int(argv[1])
except Exception as e:
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)


def solve_nqueens(n: int) -> None:
    """Place n non-attacking queens in a chessboard."""
    cols = set()
    pos_diag = set()
    neg_diag = set()
    result = []
    board = [[[]] * n for i in range(n)]

    def backtrack(r: int):
        """Implement a recursive backtracking algorithm."""
        if r == n:
            result.append([item for sub_list in board
                          for item in sub_list if item != []])
            return
        for c in range(n):
            if c in cols or r + c in pos_diag or r - c in neg_diag:
                continue
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = [r, c]
            backtrack(r + 1)

            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = []
    backtrack(0)
    for i in result:
        print(i)


if __name__ == "__main__":
    solve_nqueens(n)
