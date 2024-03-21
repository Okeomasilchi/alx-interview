#!/usr/bin/python3
"""
Defines a method that calculates the fewest
number of operations needed to result in exactly
n H characters in the file, given two operations:
Copy All and Paste.
"""


#!/usr/bin/python3
"""
Defines a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file, given two operations: Copy All
and Paste.
"""


def minOperations(n):
    """Calculates the fewest number of operations
    needed to reach n H characters."""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
