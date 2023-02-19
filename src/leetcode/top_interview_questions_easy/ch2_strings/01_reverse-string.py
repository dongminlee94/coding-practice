# -*- coding: utf-8 -*-

"""
1. Reverse String
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/879/
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        TC: O(N) / SC: O(1)
        """
        s.reverse()
