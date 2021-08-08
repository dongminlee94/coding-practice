from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        """
        N: len(students) / M: len(students[0])
        TC: O(N!M) / SC: O(M)
        Runtime: 2628 ms, faster than 33.54%
        Memory Usage: 14.2 MB, less than 95.44%
        """
        self.ans = 0

        def dfs(s_idx: int = 0, assigned: List[int] = [], scores: int = 0) -> int:
            if s_idx == len(students):
                if self.ans < scores:
                    self.ans = scores
                return

            for m_idx in range(len(students)):
                if m_idx not in assigned:
                    score = sum([s == m for s, m in zip(students[s_idx], mentors[m_idx])])
                    dfs(s_idx + 1, assigned + [m_idx], scores + score)
            return self.ans

        return dfs()
