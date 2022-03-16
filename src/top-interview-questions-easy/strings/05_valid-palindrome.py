# -*- coding: utf-8 -*-

"""
5. Valid Palindrome *
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        TC: O(N) / SC: O(N)
        """
        s = "".join(c for c in s.lower() if c.isalnum())
        return s == s[::-1]
