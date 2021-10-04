# -*- coding: utf-8 -*-

"""
1980. Find Unique Binary String
https://leetcode.com/problems/find-unique-binary-string/

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Reference:
https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument
"""
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        TC: O(N) / SC: O(N)
        """
        ans = []
        for i, num in enumerate(nums):
            ans.append("1" if num[i] == "0" else "0")
        return "".join(ans)
