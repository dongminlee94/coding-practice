# -*- coding: utf-8 -*-

"""
3. Maximum Subarray
https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
"""


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        TC: O(N) / SC: O(1)
        """
        cur, ans = 0, -float("inf")
        for n in nums:
            cur += n
            if cur < n:
                cur = n

            if ans < cur:
                ans = cur
        return ans
