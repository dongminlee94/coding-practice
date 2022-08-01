# -*- coding: utf-8 -*-

"""
4. Contains Duplicate
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        TC: O(N) / SC: O(N)
        """
        return len(nums) != len(set(nums))
