# -*- coding: utf-8 -*-

"""
2013. Detect Squares
https://leetcode.com/problems/detect-squares/

Example 1:

Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]

Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
-> defaultdict(<class 'collections.Counter'>, {3: Counter({10: 1, 2: 1}), 11: Counter({2: 1})})

detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
-> defaultdict(<class 'collections.Counter'>, {3: Counter({10: 1, 2: 1}), 11: Counter({2: 2}), 19: Counter(), 14: Counter()})

detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points
"""
import collections
from typing import List


class DetectSquares:
    def __init__(self):
        self.square = collections.defaultdict(collections.Counter)

    def add(self, point: List[int]) -> None:
        """
        N: len(the number of add calls)
        SC: O(N)
        """
        self.square[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        """
        M: len(the number of count calls)
        TC: O(M * N)
        """
        ans = 0
        for y in self.square[point[0]]:
            if point[1] != y:
                y_interval = abs(point[1] - y)
                for interval in [-y_interval, y_interval]:
                    point_1 = self.square[point[0]][y]  # In -y_interval, bottom right
                    point_2 = self.square[point[0] + interval][y]  # Bottom left
                    point_3 = self.square[point[0] + interval][point[1]]  # Top left
                    ans += point_1 * point_2 * point_3
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
