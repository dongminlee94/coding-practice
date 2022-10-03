# -*- coding: utf-8 -*-

"""
4. Longest Substring Without Repeating Characters
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        TC: O(N) / SC: O(N)
        """
        q, ans = [], 0
        for c in s:
            if c in q:
                q = q[q.index(c) + 1 :]

            q.append(c)
            assert len(q) == len(set(q)), "The elements of the queue must be unique."

            ans = len(q) if ans < len(q) else ans
        return ans
