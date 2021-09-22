# -*- coding: utf-8 -*-

"""
1979. Find Greatest Common Divisor of Array
https://leetcode.com/problems/find-greatest-common-divisor-of-array/

Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

Example 2:

Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

Example 3:

Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.

Reference: math.gcd
https://codility.com/media/train/10-Gcd.pdf
"""
import math
from typing import List


class Solution:
    """
    TC: O(N) / SC: O(1)
    """

    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(min(nums), max(nums))
