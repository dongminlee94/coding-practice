class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join(str(ord(i)-96) for i in s)
        for i in range(k):
            s = str(sum(int(j) for j in s))
        return s