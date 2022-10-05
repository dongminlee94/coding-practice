# -*- coding: utf-8 -*-

"""
5. Longest Palindromic Substring *
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        TC: O(N) / SC: O(N)
        """
        if s == s[::-1]:
            return s

        start, size = 0, 1
        for i in range(1, len(s)):
            left = i - size
            sub_s1, sub_s2 = s[left - 1 : i + 1], s[left : i + 1]

            if left - 1 >= 0 and sub_s1 == sub_s1[::-1]:
                start, size = left - 1, size + 2
            elif sub_s2 == sub_s2[::-1]:
                start, size = left, size + 1
        return s[start : start + size]
