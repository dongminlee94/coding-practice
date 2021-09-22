# -*- coding: utf-8 -*-

"""
1996. The Number of Weak Characters in the Game
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

Example 1:

Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
After sorting: [[6,3],[5,5],[3,6]]

Example 2:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
After sorting: [[3,3],[2,2]]

Example 3:

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
After sorting: [[10,4],[4,3],[1,5]]

Example 4:

Input: properties = [[2,1],[2,2],[1,1],[1,2]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
After sorting: [[2,1],[2,2],[1,1],[1,2]]

Reference:
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/1445198/Python-Sort
"""

from typing import List


class Solution:
    def numberOfWeakCharacters1(self, properties: List[List[int]]) -> int:
        """
        Time Limit Exceeded
        """
        ans = 0
        for i in range(len(properties)):
            for j in range(len(properties)):
                if properties[i][0] < properties[j][0] and properties[i][1] < properties[j][1]:
                    ans += 1
                    break
        return ans

    def numberOfWeakCharacters2(self, properties: List[List[int]]) -> int:
        """
        N: len(properties)
        TC: O(NlogN) / SC: O(1)
        """
        ans = 0
        properties.sort(key=lambda x: (-x[0], x[1]))

        max_value = 0
        for prop in properties:
            if prop[1] < max_value:
                ans += 1
            else:
                max_value = prop[1]
        return ans
