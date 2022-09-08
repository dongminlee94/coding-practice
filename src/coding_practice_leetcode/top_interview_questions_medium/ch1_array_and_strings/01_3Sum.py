# -*- coding: utf-8 -*-

"""
1. 3Sum
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        TC: O(N^2) / SC: O(N)
        """
        nums.sort()  # O(NlogN)
        ans = set()
        for i in range(len(nums)):  # O(N)
            left = i + 1
            right = len(nums) - 1

            while left < right:  # O(N)
                sum_value = nums[i] + nums[left] + nums[right]

                if sum_value == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    right -= 1
                    left += 1
                elif sum_value > 0:
                    right -= 1
                else:
                    left += 1
        return ans
