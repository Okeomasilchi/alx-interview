#!/usr/bin/python3
"""
Defines a method that calculates the fewest
number of operations needed to result in exactly
n H characters in the file, given two operations:
Copy All and Paste.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H character
    in the file.

    Args:
      n (int): The target number of H characters.

    Returns:
      int: The minimum number of operations.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
