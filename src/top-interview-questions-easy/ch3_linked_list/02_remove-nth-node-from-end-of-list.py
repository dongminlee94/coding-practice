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
        fast = head
        for _ in range(n):
            fast = fast.next

        if not fast:  # When n is the first node and the length of a head
            return head.next

        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
