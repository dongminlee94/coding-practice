# -*- coding: utf-8 -*-

"""
6. String to Integer (atoi) *
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        """
        TC: O(N) / SC: O(N)
        """
        s = s.lstrip()
        sign = False
        ans = ""
        for c in s:
            if c == "-" or c == "+":
                if not sign:
                    ans += c
                    sign = True
                else:
                    break
            elif c.isdigit():
                ans += c
                sign = True
            else:
                break

        if not ans or (len(ans) == 1 and not ans[0].isdigit()):
            return 0
        else:
            ans = int(ans)
            if ans > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif ans < -(2 ** 31):
                return -(2 ** 31)
            else:
                return ans
