#!/usr/bin/python3
"""
island_perimeter(grid): returns the
perimeter of the island described in grid
"""

from typing import List


def island_perimeter(grid: List[int]) -> int:
    """
    Calculates the perimeter of an island represented
    by a grid.

    Args:
        grid (List[int]): A 2D grid representing the
            island, where 1 represents land and 0
            represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1

    return perimeter
