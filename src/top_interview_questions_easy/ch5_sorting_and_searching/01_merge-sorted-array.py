# -*- coding: utf-8 -*-

"""
1. Merge Sorted Array
https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
"""


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        N: The number of m + n
        TC: O(NlogN) / SC: O(1)
        """
        len_nums1 = len(nums1)
        while len_nums1 != m:
            nums1.pop()
            len_nums1 = len(nums1)

        len_nums2 = len(nums2)
        while len_nums2 != n:
            nums2.pop()
            len_nums2 = len(nums2)

        nums1 += nums2
        nums1.sort()
