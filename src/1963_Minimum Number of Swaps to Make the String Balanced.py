"""
1963. Minimum Number of Swaps to Make the String Balanced
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

Example 1:

Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".

Example 2:

Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".

Example 3:

Input: s = "[]"
Output: 0
Explanation: The string is already balanced.

Reference:
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/discuss/1401218/Very-simple-Python-solution
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        """
        TC: O(N) / SC: O(1)
        """
        balance, ans = 0, 0
        for i in range(len(s)):
            if s[i] == "[":
                balance -= 1
            else:
                balance += 1
            if balance > 0:
                ans += 1
                balance = -1
        return ans
