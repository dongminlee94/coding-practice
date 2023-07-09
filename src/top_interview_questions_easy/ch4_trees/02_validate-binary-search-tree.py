# -*- coding: utf-8 -*-

"""
2. Validate Binary Search Tree *
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        N: The number of nodes
        TC: O(N) / SC: O(N)
        """
        stack = []
        trav = root
        prev = -float("inf")
        while trav or stack:
            if trav:  # Always start traversal with the left
                stack.append(trav)
                trav = trav.left
            else:  # When trav is None
                node = stack.pop()
                if node:
                    if node.val <= prev:
                        return False
                    prev = node.val
                trav = node.right
        return True
