# -*- coding: utf-8 -*-


def solution(s):
    pd_list = [0] * len(s)
    i, pd_idx = 1, 0
    while i < len(s):
        if s[i] == s[pd_idx]:
            pd_idx += 1
            pd_list[i] = pd_idx
            i += 1
        elif pd_idx > 0:
            pd_idx = pd_list[pd_idx - 1]
        else:
            pd_list[i] = 0
            i += 1
    return len(s) - pd_list[len(s) - 1] if len(s) % (len(s) - pd_list[len(s) - 1]) == 0 else len(s)


assert solution(s="abababab") == 2
assert solution(s="abcabcabd") == 9
