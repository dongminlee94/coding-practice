# -*- coding: utf-8 -*-

"""
1995. Count Special Quadruplets
https://leetcode.com/problems/count-special-quadruplets/

Example 1:

Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.

Example 2:

Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].

Example 3:

Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5
"""
import itertools
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        N: len(nums)
        TC: O(N^4) / SC: O(2 * 4) <- (index + value) * 4
        """
        ans = 0
        for quad in itertools.combinations(enumerate(nums), 4):
            if (
                quad[0][0] < quad[1][0] < quad[2][0] < quad[3][0]
                and quad[0][1] + quad[1][1] + quad[2][1] == quad[3][1]
            ):
                ans += 1
        return ans
