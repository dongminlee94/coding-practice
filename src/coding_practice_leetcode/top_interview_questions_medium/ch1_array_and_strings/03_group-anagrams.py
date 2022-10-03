# -*- coding: utf-8 -*-

"""
3. Group Anagrams
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/
"""


import collections
import functools
from typing import List, Union


class Solution:
    def set_ddict(
        self,
        default_factory: Union[int, float, str, tuple, list, dict, set, frozenset],
        depth: int = 1,
    ):
        ddict = functools.partial(collections.defaultdict, default_factory)
        for _ in range(depth - 1):
            ddict = functools.partial(collections.defaultdict, ddict)
        return ddict()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        N: len(strs)
        TC: O(N) / SC: O(N)
        """
        strs_dict: collections.defaultdict[
            tuple,
            collections.defaultdict[tuple, list[int]],
        ] = self.set_ddict(list, 2)
        for s in strs:  # TC: O(N)
            s_cnt = collections.Counter("".join(sorted(s)))  # TC: O(1)
            strs_dict[tuple(s_cnt.keys())][tuple(s_cnt.values())].append(s)

        ans = []
        for str_dict in strs_dict.values():  # TC: O(N)
            ans.extend(list(str_dict.values()))
        return ans
