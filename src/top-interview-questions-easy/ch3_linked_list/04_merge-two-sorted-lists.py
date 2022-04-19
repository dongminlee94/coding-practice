# -*- coding: utf-8 -*-

"""
4. Merge Two Sorted Lists
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        The number of nodes in both lists is in the range [0, 50].

        TC: O(1) / SC: O(1)
        """
        if not list1:
            return list2
        elif not list2:
            return list1

        ans = ListNode()
        temp1, temp2, ans1 = list1, list2, ans
        while True:
            val1 = temp1.val if temp1 else 101
            val2 = temp2.val if temp2 else 101

            if val1 <= val2:
                ans1.val = val1
                temp1 = temp1.next
            else:
                ans1.val = val2
                temp2 = temp2.next

            if not (temp1 or temp2):
                break

            ans1.next = ListNode()
            ans1 = ans1.next
        return ans
