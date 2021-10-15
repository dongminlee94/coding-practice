# -*- coding: utf-8 -*-

"""
2027. Minimum Moves to Convert String
https://leetcode.com/problems/minimum-moves-to-convert-string/

Example 1:

Input: s = "XXX"
Output: 1
Explanation: XXX -> OOO
We select all the 3 characters and convert them in one move.

Example 2:

Input: s = "XXOX"
Output: 2
Explanation: XXOX -> OOOX -> OOOO
We select the first 3 characters in the first move, and convert them to 'O'.
Then we select the last 3 characters and convert them so that the final string contains all 'O's.

Example 3:

Input: s = "OOOO"
Output: 0
Explanation: There are no 'X's in s to convert.
"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        """
        TC: O(N) / SC: O(1)
        """
        ans = 0
        skip_num = 3
        for i in range(len(s)):
            if i > 0 and skip_num:
                skip_num -= 1
                continue

            if s[i] == "X":
                ans += 1
                skip_num = 2
            else:
                skip_num = 0
        return ans
