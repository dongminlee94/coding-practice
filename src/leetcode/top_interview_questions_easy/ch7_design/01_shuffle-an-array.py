# -*- coding: utf-8 -*-

"""
1. Shuffle an Array
https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/
"""


import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        TC: O(1) / SC: O(1)
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        TC: O(N) / SC: O(1)
        """
        return random.sample(self.nums, len(self.nums))
