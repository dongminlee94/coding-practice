# -*- coding: utf-8 -*-

"""
8. Longest Common Prefix
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        N: len(strs) / M: len(min(strs, key=len))
        TC: O(N) / SC: O(M)
        """
        ans = ""
        for i in range(len(min(strs, key=len))):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return ans
            ans += char
        return ans
