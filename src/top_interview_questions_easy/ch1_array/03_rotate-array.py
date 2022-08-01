# -*- coding: utf-8 -*-

"""
3. Rotate Array
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        TC: O(k) / SC: O(1)
        """
        while k:
            nums.insert(0, nums.pop())
            k -= 1

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        TC: O(1) / SC: O(N)
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k :] + nums[: n - k]
