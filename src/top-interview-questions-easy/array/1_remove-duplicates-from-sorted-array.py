# -*- coding: utf-8 -*-

"""
1. Remove Duplicates from Sorted Array
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        TC: O(N) / SC: O(1)
        """
        idx = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[idx] = nums[i]
                idx += 1
        return idx
