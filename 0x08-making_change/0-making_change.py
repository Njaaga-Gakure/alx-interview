#!/usr/bin/python3
"""Making change."""


from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determine the least coins needed to meet a given amount.

    args:
        coins (list): list of coins
        total (int): the sum total
    returns:
        least number of coins to make the total.

    """
    if total <= 0:
        return 0
    total_cp = total
    number_of_coins = 0
    for coin in sorted(coins, reverse=True):
        while(coin <= total_cp):
            total_cp -= coin
            number_of_coins += 1
            if total_cp == 0:
                return number_of_coins
    return -1
