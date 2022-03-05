# -*- coding: utf-8 -*-

"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        TC: O(N) / SC: O(N)
        """
        sum_dict = {}
        for i, num in enumerate(numbers):
            if num in sum_dict:
                return [sum_dict[num] + 1, i + 1]
            sum_dict[target - num] = i

    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        """
        TC: O(NlogN) / SC: O(1)
        """
        for idx in range(len(numbers)):  # O(N)
            new_target = target - numbers[idx]
            left, right = idx + 1, len(numbers) - 1
            while left <= right:  # O(logN)
                mid = left + (right - left) // 2

                if numbers[mid] == new_target:
                    return [idx + 1, mid + 1]
                elif numbers[mid] < new_target:
                    left = mid + 1
                else:
                    right = mid - 1
