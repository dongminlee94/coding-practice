# -*- coding: utf-8 -*-

"""
2001. Number of Pairs of Interchangeable Rectangles
https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

Example 1:

Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
Output: 6
Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
- Rectangle 0 with rectangle 1: 4/8 == 3/6.
- Rectangle 0 with rectangle 2: 4/8 == 10/20.
- Rectangle 0 with rectangle 3: 4/8 == 15/30.
- Rectangle 1 with rectangle 2: 3/6 == 10/20.
- Rectangle 1 with rectangle 3: 3/6 == 15/30.
- Rectangle 2 with rectangle 3: 10/20 == 15/30.

Example 2:

Input: rectangles = [[4,5],[7,8]]
Output: 0
Explanation: There are no interchangeable pairs of rectangles.
"""
import collections
import math
from typing import List


class Solution:
    def interchangeableRectangles1(self, rectangles: List[List[int]]) -> int:
        """
        Time Limit Exceeded
        """
        for i in range(len(rectangles)):  # TC: O(N)
            gcd_value = math.gcd(rectangles[i][0], rectangles[i][1])
            rectangles[i][0] = int(rectangles[i][0] / gcd_value)
            rectangles[i][1] = int(rectangles[i][1] / gcd_value)

        ans = 0
        for i in range(len(rectangles)):  # TC: O(N)
            ans += rectangles[i + 1 :].count(rectangles[i])  # TC: O(N)
        return ans

    def interchangeableRectangles2(self, rectangles: List[List[int]]) -> int:
        """
        N: len(rectangles)
        TC: O(N) / SC: O(N)
        """
        for i in range(len(rectangles)):  # TC: O(N)
            gcd_value = math.gcd(rectangles[i][0], rectangles[i][1])
            rectangles[i][0] = int(rectangles[i][0] / gcd_value)
            rectangles[i][1] = int(rectangles[i][1] / gcd_value)

        ans = 0
        count_dict = collections.defaultdict(int)  # SC: O(N)
        for rect in rectangles:  # TC: O(N)
            ans += count_dict[str(rect)]
            count_dict[str(rect)] += 1
        return ans
