#!/usr/bin/python3
"""Prime Game."""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def has_prime(num_set):
    for num in num_set:
        if is_prime(num):
            return True
    return False


def isWinner(x, nums):
    """Return the winner of a prime game."""
    player = 'Maria'
    round_wins = {'Ben': 0, 'Maria': 0}
    is_game_on = True
    for i in range(x):
        int_set = {num for num in range(1, nums[i] + 1)}
        while(is_game_on):
            if not has_prime(int_set):
                is_game_on = False
                player = "Ben" if player == 'Maria' else "Maria"
                break
            for k in int_set:
                if is_prime(k):
                     for j in int_set.copy():
                         if j % k == 0:
                             int_set.remove(j)
                     break
            player = "Ben" if player == 'Maria' else "Maria"
        if(player == 'Ben'):
            round_wins['Ben'] += 1
        else:
            round_wins['Maria'] += 1
        player = "Maria"
        is_game_on = True
    return 'Ben' if round_wins.get('Ben') > round_wins.get('Maria') else 'Maria' 
