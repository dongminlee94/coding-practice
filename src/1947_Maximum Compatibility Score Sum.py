"""
1947. Maximum Compatibility Score Sum
https://leetcode.com/problems/maximum-compatibility-score-sum/

Example 1:

Input: students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
Output: 8
Explanation: We assign students to mentors in the following way:
- student 0 to mentor 2 with a compatibility score of 3.
- student 1 to mentor 0 with a compatibility score of 2.
- student 2 to mentor 1 with a compatibility score of 3.
The compatibility score sum is 3 + 2 + 3 = 8.

Example 2:

Input: students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]
Output: 0
Explanation: The compatibility score of any student-mentor pair is 0.
"""

from typing import List


class Solution:
    def maxCompatibilitySum1(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        """
        M: len(students) / N: len(students[0])
        TC: O(M! * N^2) / SC: O(M^2)
        """
        self.ans = 0

        def dfs(s_idx: int = 0, assigned: List[int] = [], scores: int = 0) -> int:
            if s_idx == len(students):
                if self.ans < scores:
                    self.ans = scores
                return

            for m_idx in range(len(students)):
                if m_idx not in assigned:  # TC: O(N)
                    score = sum([s == m for s, m in zip(students[s_idx], mentors[m_idx])])
                    dfs(s_idx + 1, assigned + [m_idx], scores + score)  # SC: O(M^2)
            return self.ans

        return dfs()

    def maxCompatibilitySum2(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        """
        M: len(students) / N: len(students[0])
        TC: O(M! * N^2) / SC: O(M)
        """
        self.ans = 0

        def dfs(s_idx: int = 0, assigned: List[int] = [], scores: int = 0) -> int:
            if s_idx == len(students):
                if self.ans < scores:
                    self.ans = scores
                return

            for m_idx in range(len(students)):
                if m_idx not in assigned:  # TC: O(N)
                    score = sum([s == m for s, m in zip(students[s_idx], mentors[m_idx])])
                    assigned.append(m_idx)
                    dfs(s_idx + 1, assigned, scores + score)  # SC: O(M)
                    assigned.pop()
            return self.ans

        return dfs()
