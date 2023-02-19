# -*- coding: utf-8 -*-

"""
7. Plus One
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/559/
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        TC: O(N) / SC: O(N)
        """
        return list(str(int("".join(map(str, digits))) + 1))
