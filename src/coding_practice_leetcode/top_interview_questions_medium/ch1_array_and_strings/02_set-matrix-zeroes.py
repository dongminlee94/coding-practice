# -*- coding: utf-8 -*-

"""
2. Set Matrix Zeroes
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
"""


import collections
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        M: len(matrix) / N: len(matrix[0])
        TC: O(M * N) / SC: O(1)
        """
        mark = collections.defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    mark["r"].add(i)
                    mark["c"].add(j)

        for i in mark["r"]:
            matrix[i] = [0] * len(matrix[0])

        for j in mark["c"]:
            for i in range(len(matrix)):
                matrix[i][j] = 0
