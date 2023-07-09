# -*- coding: utf-8 -*-

"""
1. Maximum Depth of Binary Tree
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        N: The maximum depth of tree
        TC: O(2^N) / SC: O(N)
        """

        def recur(tree: Optional[TreeNode], depth: int) -> int:
            if not tree:
                return depth
            return max(recur(tree.left, depth + 1), recur(tree.right, depth + 1))

        return recur(root, 0)
