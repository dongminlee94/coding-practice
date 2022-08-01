# -*- coding: utf-8 -*-

"""
4. Binary Tree Level Order Traversal *
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        N: The number of nodes
        TC: O(N) / SC: O(N)
        """
        if not root:
            return []

        ans_list, queue = [], [root]
        while queue:
            level_list = []
            for _ in range(len(queue)):
                # Take all the nodes out of the queue and deal with them
                node = queue.pop(0)
                level_list.append(node.val)

                # Add the left node and the right node in the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans_list.append(level_list)
        return ans_list
