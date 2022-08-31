# -*- coding: utf-8 -*-

"""
3. Reverse Bits
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        """
        TC: O(1) / SC: O(1)
        """
        bit = f"{n:b}"[::-1]
        return int(bit + "0" * (32 - len(bit)), 2)
