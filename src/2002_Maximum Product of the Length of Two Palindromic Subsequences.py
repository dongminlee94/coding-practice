# -*- coding: utf-8 -*-

"""
2002. Maximum Product of the Length of Two Palindromic Subsequences
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

Example 1:

Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.

Example 2:

Input: s = "bb"
Output: 1
Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
The product of their lengths is: 1 * 1 = 1.

Example 3:

Input: s = "accbcaxxcxx"
Output: 25
Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
The product of their lengths is: 5 * 5 = 25.

Reference:
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/discuss/1458544/Python-Clean-and-Simple-bitmask
"""


class Solution:
    def maxProduct(self, s: str) -> int:
        """
        N: len(s)
        TC: O(2^N * N) / SC: O(2 * 2^N + N)
        """
        # len(s) <= 12, which means the search space is small
        arr = []
        for mask in range(1, 1 << len(s)):  # 1 << len(s): range(1, 2^n)
            subseq = []
            for i in range(len(s)):  # TC: O(N)
                # Convert the bitmask to the actual subsequence
                if mask & (1 << i) > 0:  # (1 << i): 2^0, 2^1, ..., 2^10
                    subseq.append(s[i])  # SC: N

            # Check whether a subseq is palindromic or not
            if subseq == subseq[::-1]:
                arr.append((mask, len(subseq)))  # SC: 2 * 2^N

        arr.sort(key=lambda x: x[1], reverse=True)  # TC: NlogN

        ans = 1
        for i in range(len(arr)):  # TC: O(2^N)
            i_mask, i_len = arr[i]

            # Break early
            if i_len ** 2 < ans:
                break

            for j in range(i + 1, len(arr)):  # TC: O(N)
                j_mask, j_len = arr[j]

                # Check whether arr[i] and arr[j] are disjoint or not
                if i_mask & j_mask == 0 and i_len * j_len > ans:
                    ans = i_len * j_len
                    break
        return ans
