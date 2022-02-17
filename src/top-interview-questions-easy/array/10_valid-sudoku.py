# -*- coding: utf-8 -*-

"""
10. Valid Sudoku *
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        N = len(board) * len(board[0])
        TC: O(N) / SC: O(N)
        """
        row_chk = [set() for _ in range(9)]
        col_chk = [set() for _ in range(9)]
        box_chk = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                k = ((i // 3) * 3) + (j // 3)
                if (
                    (board[i][j] in row_chk[i])
                    or (board[i][j] in col_chk[j])
                    or (board[i][j] in box_chk[k])
                ):
                    return False

                row_chk[i].add(board[i][j])
                col_chk[j].add(board[i][j])
                box_chk[k].add(board[i][j])
        return True
