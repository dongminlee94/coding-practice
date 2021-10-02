# -*- coding: utf-8 -*-

"""
2012. Sum of Beauty in the Array
https://leetcode.com/problems/sum-of-beauty-in-the-array/

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.
right_min: [3, 3, 3]

Example 2:

Input: nums = [2,4,6,4]
Output: 1
Explanation: For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.
right_min: [4, 4, 4, 4]

Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 0.
right_min: [1, 1, 1]

Example 4:
Input: nums = [6,8,3,7,8,9,4,8]
Output: 2
Explanation: For each index i in the range 1 <= i <= 6:
- The beauty of nums[3] equals 1.
- The beauty of nums[4] equals 1.
right_min: [8, 3, 4, 4, 4, 4, 8, 8]

Example 5:
Input: nums = [3,48,33,17,21,95,24,67,89,1,50,76,6,32,20,5,1,45,79,81,96,96,15,37,44,63,4,40,58,71,99,78,95,6,34,97,52,80,91,20,61,29,12,85,88,41,14,4,58,17,67,75,100,51,63,66,42,19,44,34,34,78,54,84,3,90,72,18,86,8,33,5,17,21,22,13,59,82,30,66,91,5,32,30,92,57,10,33,11,76,30,80,80,91,47,33]
Output: 21
Explanation: For each index i in the range 1 <= i <= 95:
- The beauty of nums[4] equals 1.
- The beauty of nums[7] equals 1.
- The beauty of nums[10] equals 1.
- The beauty of nums[17] equals 1.
- The beauty of nums[18] equals 1.
- The beauty of nums[19] equals 1.
- The beauty of nums[23] equals 1.
- The beauty of nums[24] equals 1.
- The beauty of nums[27] equals 1.
- The beauty of nums[28] equals 1.
- The beauty of nums[29] equals 1.
- The beauty of nums[34] equals 1.
- The beauty of nums[37] equals 1.
- The beauty of nums[43] equals 1.
- The beauty of nums[50] equals 1.
- The beauty of nums[51] equals 1.
- The beauty of nums[54] equals 1.
- The beauty of nums[72] equals 1.
- The beauty of nums[73] equals 1.
- The beauty of nums[76] equals 1.
- The beauty of nums[79] equals 1.
right_min: [33, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 11, 11, 30, 30, 33, 33, 33, 33, 33, 33]

Reference:
https://leetcode.com/problems/sum-of-beauty-in-the-array/discuss/1489396/Python-simple-approachexplained-beats-89
"""
from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        """
        N: len(nums)
        TC: O(N) / SC: O(N)
        """
        right_min = [nums[-1]] * len(nums)
        for i in reversed(range(1, len(nums) - 1)):
            right_min[i] = min(nums[i + 1], right_min[i + 1])

        ans, left_max = 0, nums[0]
        for i in range(1, len(nums) - 1):
            if left_max < nums[i] < right_min[i]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1

            left_max = max(left_max, nums[i])
        return ans
