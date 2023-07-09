# -*- coding: utf-8 -*-

"""
5. Valid Parentheses
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        TC: O(N) / SC: O(N)
        """
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False

        brackets = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        buf = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                buf.append(c)
            else:
                if buf:
                    if brackets[buf.pop()] == c:
                        continue
                    else:
                        return False
                else:
                    return False

        if buf:
            return False
        else:
            return True
