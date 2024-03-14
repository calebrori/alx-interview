#!/usr/bin/python3
"""
Prime numbers game
"""


def primeNumbers(n):
    """set of integers starting from 1 up to and n
       Args:
        x is the number of rounds and nums is an array of n
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos


def isWinner(x, nums):
    """
    Winner determined
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        name of the player that won the most rounds
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
