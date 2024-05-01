#!/usr/bin/python3
"""
Module for computing the fewest number of coins needed
to meet a given amount total.
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Computes the fewest number of coins needed to meet
    a given amount total.

    Args:
        coins (list): List of coin denominations.
        total (int): Total amount to be achieved.

    Returns:
        int: Fewest number of coins needed to meet the total.
             Returns -1 if the total cannot be achieved.
    """
    # Create a list to store the minimum number of coins for
    # each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update the dp array to find minimum coins needed for
        # each amount up to total
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # The result will be the minimum number of coins needed for
    # the total amount
    return dp[total] if dp[total] != float('inf') else -1
