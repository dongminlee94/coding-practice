"""
1953. Maximum Number of Weeks for Which You Can Work
https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

Example 1:

Input: milestones = [1,2,3]
Output: 6
Explanation: One possible scenario is:
​​​​- During the 1st week, you will work on a milestone of project 0.
- During the 2nd week, you will work on a milestone of project 2.
- During the 3rd week, you will work on a milestone of project 1.
- During the 4th week, you will work on a milestone of project 2.
- During the 5th week, you will work on a milestone of project 1.
- During the 6th week, you will work on a milestone of project 2.
The total number of weeks is 6.

Example 2:

Input: milestones = [5,2,1]
Output: 7
Explanation: One possible scenario is:
- During the 1st week, you will work on a milestone of project 0.
- During the 2nd week, you will work on a milestone of project 1.
- During the 3rd week, you will work on a milestone of project 0.
- During the 4th week, you will work on a milestone of project 1.
- During the 5th week, you will work on a milestone of project 0.
- During the 6th week, you will work on a milestone of project 2.
- During the 7th week, you will work on a milestone of project 0.
The total number of weeks is 7.
Note that you cannot work on the last milestone of project 0 on 8th week because it would violate the rules.
Thus, one milestone in project 0 will remain unfinished.
"""

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
