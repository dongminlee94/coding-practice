class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """
        TC: O(N) / SC: O(1)
        Runtime: 32 ms, faster than 90.10%
        Memory Usage: 14.2 MB, less than 82.93%
        """
        s = "".join(str(ord(i) - 96) for i in s)
        for _ in range(k):
            s = str(sum(list(map(int, s))))
        return s
