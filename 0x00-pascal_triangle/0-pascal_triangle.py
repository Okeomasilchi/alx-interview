#!/usr/bin/python3
"""
def pascal_triangle(n):
  Returns an empty list if n <= 0
  You can assume n will be always an integer
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
      n (int): The number of rows to generate in Pascal's triangle.

    Returns:
      list: A list of lists representing Pascal's triangle.

    Example:
      >>> pascal_triangle(5)
      [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
