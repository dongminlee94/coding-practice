# -*- coding: utf-8 -*-

"""
220. Contains Duplicate III
https://leetcode.com/problems/contains-duplicate-iii/
"""

import collections
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        TC: O(N) / SC: O(k)
        """
        nums_dict = collections.OrderedDict()
        for num in nums:
            while len(nums_dict) > k:  # Condition k
                nums_dict.popitem(last=False)  # First item is popped

            idx = num // (t + 1)  # Unique index
            if (
                (idx in nums_dict)  # Condition t
                or (idx - 1 in nums_dict and abs(nums_dict[idx - 1] - num) <= t)
                or (idx + 1 in nums_dict and abs(nums_dict[idx + 1] - num) <= t)
            ):
                return True

            nums_dict[idx] = num
        return False
