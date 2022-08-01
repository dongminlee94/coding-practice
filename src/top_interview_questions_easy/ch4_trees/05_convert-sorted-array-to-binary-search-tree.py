# -*- coding: utf-8 -*-

"""
5. Convert Sorted Array to Binary Search Tree *
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        TC: O(N) / SC: O(logN)
        """

        def list_to_bst(nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None

            mid = len(nums) // 2
            node = TreeNode(nums[mid])

            node.left = list_to_bst(nums[:mid])
            node.right = list_to_bst(nums[mid + 1 :])
            return node

        return list_to_bst(nums)
