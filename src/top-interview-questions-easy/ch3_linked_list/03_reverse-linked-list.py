# -*- coding: utf-8 -*-

"""
3. Reverse Linked List
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        N: The number of nodes
        TC: O(N) / SC: O(N)
        """
        if not head:
            return head

        vals = []
        temp = head
        while temp:
            vals.append(temp.val)
            temp = temp.next

        ans = ListNode()
        temp = ans
        for i in reversed(range(len(vals))):
            temp.val = vals[i]
            if i != 0:
                temp.next = ListNode()
                temp = temp.next
        return ans
