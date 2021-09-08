"""
1962. Remove Stones to Minimize the Total
https://leetcode.com/problems/remove-stones-to-minimize-the-total/

Example 1:

Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.

Example 2:

Input: piles = [4,3,6,7], k = 3
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3,3,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,4].
- Apply the operation on pile 0. The resulting piles are [2,3,3,4].
The total number of stones in [2,3,3,4] is 12.
"""

import heapq
import math
from typing import List


class Solution:
    def minStoneSum1(self, piles: List[int], k: int) -> int:
        """
        Time Limit Exceeded
        """
        for _ in range(k):
            piles = sorted(piles, reverse=True)
            piles[0] = math.ceil(piles[0] / 2)
        return sum(piles)

    def minStoneSum2(self, piles: List[int], k: int) -> int:
        """
        N: len(piles)
        TC: O(klogN) / SC: O(N)
        """
        heap = [-p for p in piles]  # TC: O(N)
        heapq.heapify(heap)  # TC: O(N)
        for _ in range(k):  # TC: O(k)
            p = -heapq.heappop(heap)  # TC: O(logN)
            p = math.ceil(p / 2)
            heapq.heappush(heap, -p)  # TC: O(logN)
        return -sum(heap)
