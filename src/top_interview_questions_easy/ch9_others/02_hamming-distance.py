# -*- coding: utf-8 -*-

"""
2. Hamming Distance
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        N: max(bits of x, bits of y)
        TC: O(N) / SC: O(1)
        """
        x_bits, y_bits = f"{x:b}", f"{y:b}"
        x_len, y_len = len(x_bits), len(y_bits)
        if x_len < y_len:
            x_bits = x_bits.zfill(y_len)
        elif x_len > y_len:
            y_bits = y_bits.zfill(x_len)

        ans = 0
        for i, j in zip(x_bits, y_bits):
            if i != j:
                ans += 1
        return ans
