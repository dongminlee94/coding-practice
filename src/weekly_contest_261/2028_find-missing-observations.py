# -*- coding: utf-8 -*-

"""
2028. Find Missing Observations
https://leetcode.com/problems/find-missing-observations/

Example 1:

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.

Example 2:

Input: rolls = [1,5,6], mean = 3, n = 4
Output: [2,3,2,2]
Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.

Example 3:

Input: rolls = [1,2,3,4], mean = 6, n = 4
Output: []
Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.

Example 4:

Input: rolls = [1], mean = 3, n = 1
Output: [5]
Explanation: The mean of all n + m rolls is (1 + 5) / 2 = 3.
"""

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        N: len(rolls)
        TC: O(N) / SC: O(n)
        """
        # (sum(rolls) + x) / (len(rolls) + n) = mean
        # x = (mean * (len(rolls) + n)) - sum(rolls)
        quo, rem = divmod(mean * (len(rolls) + n) - sum(rolls), n)  # TC: O(N)
        missing_obs = [quo] * n  # SC: O(n)

        if quo <= 0 or quo > 6 or (quo == 6 and rem != 0):
            return []
        elif quo == 6 and rem == 0:
            return missing_obs
        else:
            for i in range(len(missing_obs)):  # TC: O(n)
                max_value = missing_obs[i] + rem

                if max_value > 6:
                    rem = max_value - 6
                    missing_obs[i] += 6 - missing_obs[i]
                else:
                    missing_obs[i] += rem
                    break
            return missing_obs
