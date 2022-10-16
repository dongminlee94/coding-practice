# -*- coding: utf-8 -*-

"""
6. Increasing Triplet Subsequence *
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/
"""


import bisect
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        TC: O(N) / SC: O(1)
        """
        inc = [float("inf")] * 2
        for n in nums:
            i = bisect.bisect_left(inc, n)
            if i >= 2:
                return True

            inc[i] = n
        return False
