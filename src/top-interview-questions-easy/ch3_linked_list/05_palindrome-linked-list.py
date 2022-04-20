# -*- coding: utf-8 -*-

"""
5. Palindrome Linked List
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        N: The number of nodes
        TC: O(N) / SC: O(N)
        """
        vals = []
        temp = head
        while temp:
            vals.append(temp.val)
            temp = temp.next
        return vals == vals[::-1]
