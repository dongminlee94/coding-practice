"""
1997. First Day Where You Have Been in All the Rooms
https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

Example 1:

Input: nextVisit = [0,0]
Output: 2
Explanation:
- On day 0, you visit room 0. The total times you have been in room 0 is 1, which is odd.
  On the next day you will visit room nextVisit[0] = 0
- On day 1, you visit room 0, The total times you have been in room 0 is 2, which is even.
  On the next day you will visit room (0 + 1) mod 2 = 1
- On day 2, you visit room 1. This is the first day where you have been in all the rooms.

Example 2:

Input: nextVisit = [0,0,2]
Output: 6
Explanation:
Your room visiting order for each day is: [0,0,1,0,0,1,2,...].
Day 6 is the first day where you have been in all the rooms.

Example 3:

Input: nextVisit = [0,1,2,0]
Output: 6
Explanation:
Your room visiting order for each day is: [0,0,1,1,2,2,3,...].
Day 6 is the first day where you have been in all the rooms.

Reference:
https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/discuss/1445559/Greedy-oror-4-lines-oror-Weill-Explained-oror-93-faster
"""
from typing import List


class Solution:
    def firstDayBeenInAllRooms1(self, nextVisit: List[int]) -> int:
        """
        Time Limit Exceeded
        """
        day = -1
        visit_index = 0
        visit_count = [0] * len(nextVisit)
        visit_bool = [0] * len(nextVisit)

        while not (sum(visit_bool) == len(nextVisit)):
            day += 1
            visit_count[visit_index] += 1
            if visit_bool[visit_index] < 1:
                visit_bool[visit_index] += 1

            if visit_count[visit_index] % 2 == 1:
                visit_index = nextVisit[visit_index]
            else:
                visit_index = (visit_index + 1) % len(nextVisit)
        return day

    def firstDayBeenInAllRooms2(self, nextVisit: List[int]) -> int:
        """
        TC: O(N) / SC: O(N)
        """
        modulo = 10 ** 9 + 7
        # dp: The number of days it took to reach room i starting from room 0
        dp = [0] * len(nextVisit)

        for i in range(len(nextVisit) - 1):
            # 1: going to nextVisit[i] (odd)
            # dp[i] - dp[nextVisit[i]]: coming back to same room (odd) e.g., 0,0,1, "0,0" ,1,2
            # 1: going to next room (even)
            dp[i + 1] += (dp[i] + 1 + (dp[i] - dp[nextVisit[i]]) + 1) % modulo
        return dp[-1]
