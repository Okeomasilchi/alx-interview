#!/usr/bin/python3
"""
Defines a method that calculates the fewest
number of op needed to result in exactly
n H characters in the file, given two op:
Copy All and Paste.
"""


def minOperations(n):
    """
    Calculates the fewest number of op
    needed to reach n H characters.
    """
    if n <= 1:
        return 0

    op = 0
    div = 2
    while n > 1:
        while n % div == 0:
            op += div
            n //= div
        div += 1
    return op
