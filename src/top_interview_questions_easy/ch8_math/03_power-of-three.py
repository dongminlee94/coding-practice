# -*- coding: utf-8 -*-

"""
3. Power of Three
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/
"""


import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return 3 ** round(math.log(n, 3)) == n
