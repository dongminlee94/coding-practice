"""
1954. Minimum Garden Perimeter to Collect Enough Apples
https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

Example 1:

Input: neededApples = 1
Output: 8
Explanation: A square plot of side length 1 does not contain any apples.
However, a square plot of side length 2 has 12 apples inside (as depicted in the image above).
The perimeter is 2 * 4 = 8.

Example 2:

Input: neededApples = 13
Output: 16

Example 3:

Input: neededApples = 1000000000
Output: 5040
"""


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        """
        TC: O(neededApples^(1/3)) / SC: O(1)
        Runtime: 1104 ms, faster than 56.18%
        Memory Usage: 14.1 MB, less than 90.02%
        """
        i = 1
        summedApples = 0
        while True:
            currentApples = 12 * i * i
            summedApples += currentApples
            if summedApples >= neededApples:
                return i * 2 * 4
            i += 1
