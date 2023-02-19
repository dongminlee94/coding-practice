# -*- coding: utf-8 -*-

"""
2. Count Primes *
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        TC: O(N) / SC: O(N)
        """
        sieve = [True] * n
        for i in range(2, int(n * 0.5) + 1):
            if sieve[i]:
                for j in range(i * 2, n, i):
                    sieve[j] = False
        return len([i for i in range(2, n) if sieve[i] == True])
