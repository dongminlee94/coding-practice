# -*- coding: utf-8 -*-

"""
1. 폰켓몬
https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""

import collections


def solution(nums):
    """
    TC: O(N) / SC: O(N)
    """
    return min(len(collections.Counter(nums)), len(nums) / 2)
