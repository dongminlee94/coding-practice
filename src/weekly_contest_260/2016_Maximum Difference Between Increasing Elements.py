# -*- coding: utf-8 -*-

"""
2016. Maximum Difference Between Increasing Elements
https://leetcode.com/problems/maximum-difference-between-increasing-elements/

Example 1:

Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.

Example 2:

Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].

Example 3:

Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
"""
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        """
        N: len(nums)
        TC: O(N-1) / SC: O(1)
        """
        min_value, max_diff = nums[0], -1
        for i in range(1, len(nums)):
            if min_value > nums[i]:
                min_value = nums[i]
            elif nums[i] - min_value != 0 and nums[i] - min_value > max_diff:
                max_diff = nums[i] - min_value
        return max_diff
