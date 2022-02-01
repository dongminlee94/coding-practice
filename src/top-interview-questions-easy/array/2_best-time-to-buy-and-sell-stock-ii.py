# -*- coding: utf-8 -*-

"""
2. Best Time to Buy and Sell Stock II
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        TC: O(N) / SC: O(1)
        """
        start = end = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if end >= prices[i]:
                if end - start > 0:
                    ans += end - start
                start = end = prices[i]
            else:
                end = prices[i]
        ans += end - start
        return ans
