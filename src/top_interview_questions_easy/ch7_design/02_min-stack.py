# -*- coding: utf-8 -*-

"""
2. Min Stack
https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/
"""


class MinStack:
    def __init__(self):
        """
        SC: O(N)
        """
        self.stack = []

    def push(self, val: int) -> None:
        """
        TC: O(1)
        """
        self.stack.append(val)

    def pop(self) -> None:
        """
        TC: O(1)
        """
        self.stack.pop()

    def top(self) -> int:
        """
        TC: O(1)
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        TC: O(N)
        """
        return min(self.stack)
