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
        temp1 = head
        for _ in range(n):
            temp1 = temp1.next

        if not temp1:  # When the first node is removed
            return head.next

        temp2 = head
        while temp1.next:
            temp1 = temp1.next
            temp2 = temp2.next
        temp2.next = temp2.next.next
        return head
