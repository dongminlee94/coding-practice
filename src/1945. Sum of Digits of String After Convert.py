class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join(str(ord(i)-96) for i in s)
        for _ in range(k):
            s = str(sum(list(map(int, s))))
        return s