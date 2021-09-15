"""
1986. Minimum Number of Work Sessions to Finish the Tasks
https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

Example 1:

Input: tasks = [1,2,3], sessionTime = 3
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
- Second work session: finish the third task in 3 hours.

Example 2:

Input: tasks = [3,1,3,1,1], sessionTime = 8
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish all the tasks except the last one in 3 + 1 + 3 + 1 = 8 hours.
- Second work session: finish the last task in 1 hour.

Example 3:

Input: tasks = [1,2,3,4,5], sessionTime = 15
Output: 1
Explanation: You can finish all the tasks in one work session.

Reference:
https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/discuss/1433595/Python-recursion-%2B-tuple-memoization-no-bitmask-simple-64ms
"""
from functools import lru_cache
from typing import List, Tuple


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        """
        N: len(tasks)
        TC: O(2^N * N) / SC: O(N^2)
        """
        tasks.sort()

        @lru_cache(maxsize=None)
        def dfs(tasks: Tuple[int], remainingTime: int):
            if len(tasks) == 0:
                return 1

            ans = 0
            results = []
            if tasks[0] > remainingTime:
                ans += 1
                remainingTime = sessionTime

            for i, task_time in enumerate(tasks):
                if task_time <= remainingTime:
                    results.append(dfs(tasks[:i] + tasks[i + 1 :], remainingTime - task_time))
                else:
                    break
            return ans + min(results)

        return dfs(tuple(tasks), sessionTime)
