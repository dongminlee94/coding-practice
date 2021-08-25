"""
1961. Check If String Is a Prefix of Array
https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

Example 1:

Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.

Example 2:

Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.
"""

from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        """
        TC: O(len(words)) / SC: O(1)
        Runtime: 32 ms, faster than 89.26%
        Memory Usage: 14.1 MB, less than 95.97%
        """
        w_num = 0
        for word in words:
            # 'w_num + len(word)': slicing -> pass / get, set -> error
            if s[w_num : w_num + len(word)] != word:
                return False
            w_num += len(word)
            if len(s) == w_num:
                return True
