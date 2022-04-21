# -*- coding: utf-8 -*-

"""
2. Remove Nth Node From End of List *
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        N: The number of nodes
        TC: O(N) / SC: O(1)
        """
        slow = head
        for _ in range(n):
            slow = slow.next

        if not slow:  # When the first node is removed
            return head.next

        fast = head
        while slow.next:
            slow = slow.next
            fast = fast.next
        fast.next = fast.next.next
        return head
