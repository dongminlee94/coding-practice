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
        Runtime: 1856 ms, faster than 64.12%
        Memory Usage: 28.9 MB, less than 45.63%
        """
        heap = [-p for p in piles]  # TC: O(N)
        heapq.heapify(heap)  # TC: O(N)
        for _ in range(k):  # TC: O(k)
            p = -heapq.heappop(heap)  # TC: O(logN)
            p = math.ceil(p / 2)
            heapq.heappush(heap, -p)  # TC: O(logN)
        return -sum(heap)
