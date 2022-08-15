# -*- coding: utf-8 -*-

"""
4. House Robber *
https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        TC: O(N) / SC: O(1)
        """
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
        return curr
