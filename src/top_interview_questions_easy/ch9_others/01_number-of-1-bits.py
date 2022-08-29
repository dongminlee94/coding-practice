# -*- coding: utf-8 -*-

"""
1. Number of 1 Bits
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        TC: O(N) / SC: O(N)
        """
        return len([i for i in list(f"{n:b}") if i == "1"])
