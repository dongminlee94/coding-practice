# -*- coding: utf-8 -*-

"""
1. Climbing Stairs
https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1 <= n <= 45

        TC: O(1) / SC: O(1)
        """
        if n < 4:
            return n

        dp = [1, 2, 3]
        for _ in range(4, n + 1):
            dp.append(dp[-1] + (dp[-1] - dp[-2]) + (dp[-2] - dp[-3]))
        return dp[-1]
