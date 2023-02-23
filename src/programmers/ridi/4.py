# -*- coding: utf-8 -*-


def solution(s):
    period_cnt = [0] * len(s)
    i, j = 1, 0
    while i < len(s):
        if s[i] == s[j]:
            j += 1
            period_cnt[i] = j
            i += 1
        elif j > 0:
            j = period_cnt[j - 1]
        else:
            period_cnt[i] = 0
            i += 1
    return len(s) - period_cnt[len(s) - 1] if len(s) % (len(s) - period_cnt[len(s) - 1]) == 0 else len(s)


assert solution(s="abababab") == 2
assert solution(s="abcabcabd") == 9
