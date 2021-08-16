import math


class Solution:
    """
    TC: O(logN) / SC: O(N)
    Runtime: 28 ms, faster than 94.08%
    Memory Usage: 14.2 MB, less than 72.88%
    """

    def isThree(self, n: int) -> bool:
        divisors = []
        for i in range(1, int(math.sqrt(n) + 1)):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(int(n / i))
        return len(divisors) == 3
