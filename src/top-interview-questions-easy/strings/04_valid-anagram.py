# -*- coding: utf-8 -*-

"""
4. Valid Anagram
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
"""

import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        N: max(len(s), len(t))
        TC: O(N) / SC: O(N)
        """
        return collections.Counter(s) == collections.Counter(t)
