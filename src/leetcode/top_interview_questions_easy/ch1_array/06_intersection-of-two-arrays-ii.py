# -*- coding: utf-8 -*-

"""
6. Intersection of Two Arrays II *
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/674/

OPERATOR  ||  DESCRIPTION          ||  SYNTAX
&         ||  Bitwise AND          ||  x & y
|         ||  Bitwise OR           ||  x | y
~         ||  Bitwise NOT          ||  ~x
^         ||  Bitwise XOR          ||  x ^ y
>>        ||  Bitwise right shift  ||  x>>
<<        ||  Bitwise left shift   ||  x<<
"""


import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        TC: O(N) / SC: O(N)
        """
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())
