#!/usr/bin/python3
"""
Prime Game for Alx Intervieew
"""

from typing import List, Optional


def isWinner(x: int, nums: List[int]) -> Optional[str]:
    """
    Determines the winner of the prime game.

    Args:
        x (int): The number of rounds to be played.
        nums (List[int]): A list of integers representing the
            number of stones in each round.

    Returns:
        Optional[str]: The name of the winner (either "Maria" or "Ben"),
            or None if it's a tie.
    """

    def is_prime(n: int) -> bool:
        """
        Checks if a number is prime.

        Args:
            n (int): The number to be checked.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n: int) -> List[int]:
        """
        Generates a list of prime numbers up to a given number.

        Args:
            n (int): The upper limit for generating prime numbers.

        Returns:
            List[int]: A list of prime numbers.
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_win(primes: List[int], n: int) -> bool:
        """
        Checks if a player can win a round.

        Args:
            primes (List[int]): A list of prime numbers.
            n (int): The number of stones in the round.

        Returns:
            bool: True if the player can win, False otherwise.
        """
        if n in primes:
            return True
        for prime in primes:
            if n % prime == 0:
                return True
        return False

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        primes = get_primes(nums[i])
        if can_win(primes, nums[i]):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
