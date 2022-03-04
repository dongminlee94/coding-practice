# -*- coding: utf-8 -*-

"""
9. Two Sum
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/546/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        TC: O(N^2) / SC: O(1)
        """
        for i in range(len(nums)):
            value, nums[i] = nums[i], -10
            if target - value in nums:
                return [i, nums.index(target - value)]  # O(N)

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        1) Put (target - value) in sum_dict in advance
        2) and then check if there's (target - value) in sum_dict

        TC: O(N) / SC: O(N)
        """
        sum_dict = {}
        for i, value in enumerate(nums):
            if value in sum_dict:
                return [sum_dict[value], i]
            sum_dict[target - value] = i
