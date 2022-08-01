# -*- coding: utf-8 -*-

"""
1. Delete Node in a Linked List
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: Optional[ListNode]):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        TC: O(1) / SC: O(1)
        """
        node.val, node.next = node.next.val, node.next.next
