from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        """
        TC: O(N) / SC: O(1)
        Runtime: 704 ms, faster than 97.11%
        Memory Usage: 26.5 MB, less than 70.39%
        """
        sum_value = sum(milestones)
        max_value = max(milestones)

        if sum_value >= max_value * 2:
            return sum_value
        return (sum_value - max_value) * 2 + 1
