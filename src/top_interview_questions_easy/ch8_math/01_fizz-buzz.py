# -*- coding: utf-8 -*-

"""
1. Fizz Buzz
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/
"""


from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        TC: O(N) / SC: O(N)
        """
        ans = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
