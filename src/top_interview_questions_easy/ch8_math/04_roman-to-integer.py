# -*- coding: utf-8 -*-

"""
4. Roman to Integer
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        TC: O(N) / SC: O(1)
        """
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        idx, idxs, ans = 0, len(s) - 1, 0
        while idx < idxs:
            val, next_val = s[idx], s[idx + 1]
            if (
                (val == "I" and (next_val == "V" or next_val == "X"))
                or (val == "X" and (next_val == "L" or next_val == "C"))
                or (val == "C" and (next_val == "D" or next_val == "M"))
            ):
                ans += symbols[next_val] - symbols[val]
                idx += 2
            else:
                ans += symbols[val]
                idx += 1

        if idx != len(s):
            ans += symbols[s[-1]]
        return ans
