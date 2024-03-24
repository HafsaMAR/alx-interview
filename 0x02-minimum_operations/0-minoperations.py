#!/usr/bin/python3
"""Minimum operation using greedy approach"""


def minOperations(n):
    """
    returns the min number of time to copy and paste to have
    n H string
    """
    if n <= 0:
        return 0

    operations = 0
    current = 1  # current number of H characters in the file
    copied = 0   # number of characters copied

    while current < n:
        if n % current == 0:
            copied = current
        current += copied
        operations += 1

    return operations
