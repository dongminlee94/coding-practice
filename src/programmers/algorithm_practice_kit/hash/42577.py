# -*- coding: utf-8 -*-

"""
전화번호 목록
https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""


def solution(phone_book):
    """
    TC: O(N^2) / SC: O(N)
    """
    pb_dict = dict()
    for p in phone_book:
        for i in range(1, len(p)):
            pb_dict[p[:i]] = 1

    for p in phone_book:
        if p in pb_dict:
            return False
    return True
