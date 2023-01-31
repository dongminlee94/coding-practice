# -*- coding: utf-8 -*-

"""
완주하지 못한 선수
https://school.programmers.co.kr/learn/courses/30/lessons/42576
"""

import collections


def solution(participant, completion):
    """
    TC: O(N) / SC: O(N)
    """
    part_dict, com_dict = map(collections.Counter, (participant, completion))
    for part in part_dict:
        if part_dict[part] != com_dict[part]:
            return part
