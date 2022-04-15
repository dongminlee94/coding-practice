# -*- coding: utf-8 -*-

"""
5. Valid Palindrome *
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

String isalpha(), isalnum()
isalpha(): returns true if the string is in English or Korean, or false if not.
isalnum(): returns true if the string is in English, Korean, or numeric, or false if not.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        TC: O(N) / SC: O(N)
        """
        s = "".join(c for c in s.lower() if c.isalnum())
        return s == s[::-1]
