from collections import deque

def solution(n, money):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for coin in money:
        for price in range(coin, n + 1):
            dp[price] += dp[price - coin]
            dp[price] %= 1000000007
    return dp[n]