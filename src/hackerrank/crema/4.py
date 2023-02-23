# -*- coding: utf-8 -*-

import collections


def longestChain(words):
    w_dict = collections.Counter(words)
    w_dict = sorted(w_dict)
    dp = {}

    def recur(word, cnt):
        if not word in w_dict:
            return cnt - 1
        if word in dp:
            return dp[word] + 1

        cnt_list = []
        for i in range(len(word)):
            new_cnt = recur(word[:i] + word[i + 1 :], cnt + 1)
            cnt_list.append(new_cnt)
        dp[word] = max(cnt_list)
        return max(cnt_list)

    ans = 1
    for w in w_dict:
        cnt = recur(w, 1)
        if ans < cnt:
            ans = cnt
    return ans


assert longestChain(["a", "and", "an", "bear"]) == 3
