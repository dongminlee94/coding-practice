# -*- coding: utf-8 -*-

"""
1189. Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(
            text.count("b"),
            text.count("a"),
            text.count("l") // 2,
            text.count("o") // 2,
            text.count("n"),
        )
