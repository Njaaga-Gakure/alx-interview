#!/usr/bin/python3
"""Island perimeter."""


from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Find the perimeter of an island.

    args:
        grid (list of list): a matrix with 0 as water and 1 as land
    returns:
        the perimeter of the island

    """
    island_in_grid = False
    for grid_list in grid:
        if 1 in grid_list:
            island_in_grid = True
            break
    if not island_in_grid or not grid:
        return 0

    grid_height = len(grid)
    grid_width = len(grid[0])
    p = 0

    for i in range(1, grid_height - 1):
        for j in range(1, grid_width - 1):
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
