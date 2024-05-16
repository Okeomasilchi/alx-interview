#!/usr/bin/python3
"""
Prime Game for Alx Interview

This module contains functions related to a prime game. The
game is played between two players, Maria and Ben. The game
takes a list of numbers as input and determines the winner based
on a specific set of rules.
"""


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """
    Determines the winner of a prime game.

    Args:
        x (int): The number of rounds to be played.
        nums (List[int]): A list of integers representing
            the number of elements in each round.

    Returns:
        str or None: The name of the winner (either "Maria"
        or "Ben") or None if there is no winner.
    """
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        remaining = list(range(1, n + 1))
        is_prime_list = [False] * (n + 1)
        for i in range(2, n + 1):
            if is_prime(i):
                is_prime_list[i] = True
        maria_turn = True
        while True:
            found_prime = False
            for num in remaining:
                if is_prime_list[num]:
                    prime = num
                    found_prime = True
                    break
            if not found_prime:
                break
            for multiple in range(prime, n + 1, prime):
                if multiple in remaining:
                    remaining.remove(multiple)
            if maria_turn:
                maria_turn = False
            else:
                maria_turn = True
        if maria_turn:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
