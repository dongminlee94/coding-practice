"""
1945. Sum of Digits of String After Convert
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

Example 1:

Input: s = "iiii", k = 1
Output: 36
Explanation: The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.

Example 2:

Input: s = "leetcode", k = 2
Output: 6
Explanation: The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.

Example 3:

Input: s = "zbax", k = 2
Output: 8
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """
        TC: O(N) / SC: O(N)
        Runtime: 32 ms, faster than 90.10%
        Memory Usage: 14.2 MB, less than 82.93%
        """
        s = "".join(str(ord(i) - 96) for i in s)
        for _ in range(k):
            s = str(sum(list(map(int, s))))  # SC: O(N)
        return s
