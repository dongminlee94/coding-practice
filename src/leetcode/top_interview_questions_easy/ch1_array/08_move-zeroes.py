# -*- coding: utf-8 -*-

"""
8. Move Zeroes
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/567/
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        TC: O(N) / SC: O(1)
        """
        i, cnt = 0, 0
        max_idx = len(nums) - 1
        while i != max_idx:
            if nums[i] == 0:
                nums.pop(i)
                max_idx -= 1
                cnt += 1
            else:
                i += 1
        nums.extend([0] * cnt)
