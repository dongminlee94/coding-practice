# -*- coding: utf-8 -*-

"""
2. Reverse Integer
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/880/
"""


class Solution:
    def reverse(self, x: int) -> int:
        """
        TC: O(N) / SC: O(N)
        """
        ans = -int(str(x)[1:][::-1]) if x < 0 else int(str(x)[::-1])
        return ans if -(2 ** 31) <= ans <= 2 ** 31 - 1 else 0
