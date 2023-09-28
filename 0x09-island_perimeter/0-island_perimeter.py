#!/usr/bin/python3
"""Island perimeter."""


def island_perimeter(grid):
    """
    Find the perimeter of an island.

    args:
        grid (list of list): a matrix with 0 as water and 1 as land
    returns:
        the perimeter of the island

    """
    if not grid:
        return 0

    grid_height = len(grid)
    grid_width = len(grid[0])
    p = 0

    for i in range(grid_height):
        for j in range(grid_width):
            if grid[i][j] == 1:
                p += 4
                if grid[i - 1][j] == 1:
                    p -= 1
                if grid[i + 1][j] == 1:
                    p -= 1
                if grid[i][j - 1] == 1:
                    p -= 1
                if grid[i][j + 1] == 1:
                    p -= 1
    return p
