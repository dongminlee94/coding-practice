# -*- coding: utf-8 -*-

"""
3. Symmetric Tree
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        N: The number of nodes
        TC: O(N) / SC: O(N)
        """
        l_stack, r_stack = [], []
        l_trav, r_trav = [], []
        l_node, r_node = root.left, root.right

        # Traverse the left part from the root node
        while l_node or l_trav:
            if l_node:
                l_stack.append(l_node.val)
                l_trav.append(l_node)
                l_node = l_node.left
            else:
                l_stack.append(0)
                node = l_trav.pop()
                l_node = node.right

        # Traverse the right part from the root node
        while r_node or r_trav:
            if r_node:
                r_stack.append(r_node.val)
                r_trav.append(r_node)
                r_node = r_node.right
            else:
                r_stack.append(0)
                node = r_trav.pop()
                r_node = node.left
        return l_stack == r_stack
