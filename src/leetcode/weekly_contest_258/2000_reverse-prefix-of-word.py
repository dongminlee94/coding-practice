# -*- coding: utf-8 -*-

"""
2000. Reverse Prefix of Word
https://leetcode.com/problems/reverse-prefix-of-word/

Example 1:

Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Example 2:

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

Example 3:

Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        """
        N: len(word)
        TC: O(N) / SC: O(N)
        """
        for i in range(len(word)):
            if word[i] == ch:
                return "".join(reversed(word[: i + 1])) + word[i + 1 :]
        return word
