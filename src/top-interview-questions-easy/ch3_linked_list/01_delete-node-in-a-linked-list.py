# -*- coding: utf-8 -*-

"""
1. Delete Node in a Linked List
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val, node.next = node.next.val, node.next.next
