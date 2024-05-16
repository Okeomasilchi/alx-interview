#!/usr/bin/python3
"""
Prime Game for Alx Intervieew
"""

from typing import List, Optional


from typing import List, Optional

def isWinner(x: int, nums: List[int]) -> Optional[str]:
    """
    Determines the winner of a game played over multiple rounds.

    Parameters:
    - x (int): The number of rounds played.
    - nums (List[int]): A list containing the maximum integer for each round.

    Returns:
    - Optional[str]: The name of the player who won the most rounds ('Maria' or 'Ben').
      Returns 'None' if there is a tie.

    The function implements the Sieve of Eratosthenes algorithm to determine the number of primes
    for each round and decides the winner based on the parity of the count of remaining primes.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        remaining_primes = [i for i in range(2, n + 1) if primes[i]]

        if len(remaining_primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None