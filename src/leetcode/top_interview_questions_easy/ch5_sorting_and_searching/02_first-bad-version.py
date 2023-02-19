# -*- coding: utf-8 -*-

"""
2. First Bad Version
https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
"""


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        TC: O(logN) / SC: O(1)
        """
        left = 0
        while left <= n:
            mid = (left + n) // 2
            if isBadVersion(mid):  # True
                if not isBadVersion(mid - 1):  # False
                    return mid
                else:  # True
                    n = mid - 1
            else:  # False
                if isBadVersion(mid + 1):  # True
                    return mid + 1
                else:  # False
                    left = mid + 1
