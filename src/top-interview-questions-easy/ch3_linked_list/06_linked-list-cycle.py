# -*- coding: utf-8 -*-

"""
6. Linked List Cycle *
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        TC: O(N) / SC: O(1)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
