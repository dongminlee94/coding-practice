# -*- coding: utf-8 -*-

"""
4. Pascal's Triangle
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/
"""


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        TC: O(1) / SC: O(1)
        """
        if numRows == 1:
            return [[1]]

        ans = [[1], [1, 1]]
        for _ in range(3, numRows + 1):
            prev, temp = ans[-1], []
            for i in range(1, len(prev)):
                val = prev[i - 1] + prev[i]
                temp.append(val)
            ans.append([1] + temp + [1])
        return ans
