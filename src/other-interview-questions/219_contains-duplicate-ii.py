# -*- coding: utf-8 -*-

"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/
"""

import collections
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        TC: O(N) / SC: O(N)
        """
        nums_dict = collections.defaultdict(list)
        for i, num in enumerate(nums):
            nums_dict[num] += [i]
            if len(nums_dict[num]) >= 2:
                if abs(nums_dict[num][0] - i) <= k:
                    return True
                else:
                    nums_dict[num].pop(0)
        return False

    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        """
        TC: O(N) / SC: O(N)
        """
        nums_dict = {}
        for i, num in enumerate(nums):
            if num in nums_dict and (i - nums_dict[num] <= k):
                return True
            nums_dict[num] += [i]
        return False

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        """
        TC: O(N) / SC: O(N)
        """
        nums_set = set()
        for i, num in enumerate(nums):
            if i > k:
                nums_set.remove(nums[i - k - 1])
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
