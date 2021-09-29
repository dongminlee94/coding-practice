# -*- coding: utf-8 -*-

"""
2002. Maximum Product of the Length of Two Palindromic Subsequences
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

Example 1:

Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.
arr: [(134, 3), (138, 3), (140, 3), (146, 3), (148, 3), (162, 3), (164, 3), (194, 3), (196, 3), (304, 3), (336, 3), (400, 3), (608, 3), (672, 3), (800, 3), (6, 2), (130, 2), (132, 2), (272, 2), (544, 2), (1, 1), (2, 1), (4, 1), (8, 1), (16, 1), (32, 1), (64, 1), (128, 1), (256, 1), (512, 1), (1024, 1)]

Example 2:

Input: s = "bb"
Output: 1
Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
The product of their lengths is: 1 * 1 = 1.
arr: [(3, 2), (1, 1), (2, 1)]

Example 3:

Input: s = "accbcaxxcxx"
Output: 25
Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
The product of their lengths is: 5 * 5 = 25.
arr: [(55, 5), (59, 5), (61, 5), (286, 5), (1984, 5), (39, 4), (51, 4), (53, 4), (278, 4), (450, 4), (452, 4), (464, 4), (1728, 4), (22, 3), (26, 3), (28, 3), (35, 3), (37, 3), (41, 3), (49, 3), (262, 3), (266, 3), (268, 3), (274, 3), (276, 3), (290, 3), (292, 3), (304, 3), (322, 3), (324, 3), (336, 3), (386, 3), (388, 3), (400, 3), (704, 3), (832, 3), (896, 3), (1216, 3), (1344, 3), (1408, 3), (1600, 3), (1664, 3), (6, 2), (18, 2), (20, 2), (33, 2), (192, 2), (258, 2), (260, 2), (272, 2), (576, 2), (640, 2), (1088, 2), (1152, 2), (1536, 2), (1, 1), (2, 1), (4, 1), (8, 1), (16, 1), (32, 1), (64, 1), (128, 1), (256, 1), (512, 1), (1024, 1)]

Reference:
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/discuss/1458544/Python-Clean-and-Simple-bitmask
"""


class Solution:
    def maxProduct(self, s: str) -> int:
        """
        N: len(s)
        TC: O(2^N * N) / SC: O(2^N + N)
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
                arr.append((mask, len(subseq)))  # SC: 2^N

        arr.sort(key=lambda x: x[1], reverse=True)  # TC: 2^Nlog2^N

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
