"""
1981. Minimize the Difference Between Target and Chosen Elements
https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
Output: 0
Explanation: One possible choice is to:
- Choose 1 from the first row.
- Choose 5 from the second row.
- Choose 7 from the third row.
The sum of the chosen elements is 13, which equals the target, so the absolute difference is 0.

Example 2:


Input: mat = [[1],[2],[3]], target = 100
Output: 94
Explanation: The best possible choice is to:
- Choose 1 from the first row.
- Choose 2 from the second row.
- Choose 3 from the third row.
The sum of the chosen elements is 6, and the absolute difference is 94.

Example 3:


Input: mat = [[1,2,9,8,7]], target = 6
Output: 1
Explanation: The best choice is to choose 7 from the first row.
The absolute difference is 1.

Reference:
https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/discuss/1418753/Python-Set-and-Early-Stop-(2700ms)
"""
from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        """
        M: len(mat) / N: len(mat[0])
        TC: O((M*N)^2) / SC: O(2*M*N)
        Runtime: 2214 ms, faster than 87.93%
        Memory Usage: 14.3 MB, less than 99.60%
        """
        cur_set = set([0])
        for row in mat:  # TC: O(M)
            next_set = set()
            row = sorted(set(row))  # TC: O(NlogN)

            for s in cur_set:  # TC: O(M*N)
                for col in row:  # TC: O(N)
                    next_set.add(col + s)

                    if col + s > target:
                        break
            cur_set = next_set
        return min(abs(s - target) for s in cur_set)
