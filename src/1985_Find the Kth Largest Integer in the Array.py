# -*- coding: utf-8 -*-

"""
1985. Find the Kth Largest Integer in the Array
https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

Example 1:

Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".

Example 2:

Input: nums = ["2","21","12","1"], k = 3
Output: "2"
Explanation:
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3rd largest integer in nums is "2".

Example 3:

Input: nums = ["0","0"], k = 2
Output: "0"
Explanation:
The numbers in nums sorted in non-decreasing order are ["0","0"].
The 2nd largest integer in nums is "0".
"""
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """
        TC: O(NlogN) / SC: O(N)
        """
        return str(sorted(map(int, nums), reverse=True)[k - 1])
