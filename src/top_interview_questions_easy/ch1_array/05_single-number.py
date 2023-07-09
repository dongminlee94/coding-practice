# -*- coding: utf-8 -*-

"""
5. Single Number
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/
"""

import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        TC: O(N) / SC: O(N)
        """
        check = collections.defaultdict(int)
        for n in nums:
            check[n] += 1
        for k, v in check.items():
            if v == 1:
                return k

    def singleNumber1(self, nums: List[int]) -> int:
        """
        TC: O(N) / SC: O(N)
        """
        return 2 * sum(set(nums)) - sum(nums)
