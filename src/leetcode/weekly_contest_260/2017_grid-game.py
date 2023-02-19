# -*- coding: utf-8 -*-

"""
2017. Grid Game
https://leetcode.com/problems/grid-game/

Example 1:

Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.

Example 2:

Input: grid = [[3,3,1],[8,5,2]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 3 + 1 + 0 = 4 points.

Example 3:

Input: grid = [[1,3,1,15],[1,3,3,1]]
Output: 7
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.

References:
- https://en.wikipedia.org/wiki/Minimax
- https://medium.com/tokeonomy/%EA%B2%8C%EC%9E%84%EC%9D%B4%EB%A1%A0-%EB%B2%A0%EC%9D%B4%EC%A7%81-game-theory-basic-398bbfd4f87b
- https://medium.com/tokeonomy/%EA%B2%8C%EC%9E%84%EC%9D%B4%EB%A1%A0-%EB%B2%A0%EC%9D%B4%EC%A7%81-game-theory-basic-%EC%A0%9C%EB%A1%9C%EC%84%AC%EA%B2%8C%EC%9E%84-zero-sum-game-3ad0057a8f93
"""
from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        """
        TC: O(N) / SC: O(N)
        """
        sum_first_row = sum(grid[0][1:])
        sum_second_row = 0
        max_list = [sum_first_row]

        for i in range(1, len(grid[0])):
            sum_first_row -= grid[0][i]
            sum_second_row += grid[1][i - 1]
            max_list.append(max(sum_first_row, sum_second_row))
        return min(max_list)
