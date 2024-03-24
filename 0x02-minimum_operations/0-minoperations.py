#!/usr/bin/env python3
"""Minimum operation using dynamic programming"""

def minOperations(n):
    """
    returns the min number of time to copy and paste to have
    n H string
    """
    if n == 1:
        return 0
    
    dp = [0] * (n + 1)
    for i in range (2, n+1):
        dp[i] = i
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + dp[i // j])

    return dp[n]