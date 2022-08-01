# -*- coding: utf-8 -*-

"""
7. Implement strStr() *
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        N: len(haystack) / M: len(needle)
        TC: O(N) / SC: O(M)
        """
        if not needle:
            return 0

        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
