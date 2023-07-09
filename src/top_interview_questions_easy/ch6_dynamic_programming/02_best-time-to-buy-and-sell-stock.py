# -*- coding: utf-8 -*-

"""
2. Best Time to Buy and Sell Stock
https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        TC: O(N) / SC: O(1)
        """
        max_p, min_p = -1, float("inf")
        ans = 0
        for price in prices:
            if price < min_p:
                max_p = min_p = price
            elif max_p < price:
                max_p = price
                if ans < max_p - min_p:
                    ans = max_p - min_p
        return ans
