# -*- coding: utf-8 -*-

"""
3. First Unique Character in a String
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
"""


import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        TC: O(N) / SC: O(N)
        """
        s_dict = collections.defaultdict(list)
        for i, c in enumerate(s):
            s_dict[c].append(i)

        ans = []
        for v_list in s_dict.values():
            if len(v_list) == 1:
                ans.append(v_list[0])

        if ans:
            return min(ans)
        else:
            return -1
