# -*- coding: utf-8 -*-

"""
11. Rotate Image
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/770/
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        N = len(matrix)
        TC: O(N) / SC: O(N)
        """
        for i, mat in enumerate(zip(*matrix)):
            matrix[i] = mat[::-1]
