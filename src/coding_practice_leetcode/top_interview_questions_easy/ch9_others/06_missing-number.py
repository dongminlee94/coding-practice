# -*- coding: utf-8 -*-

"""
6. Missing Number
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
"""


from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        TC: O(NlogN) / SC: O(1)
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
