# -*- coding: utf-8 -*-


def maxLength(a, k):
    for end in reversed(range(1, len(a) + 1)):
        for start in range(len(a)):
            if start + end <= len(a):
                if sum(a[start : start + end]) <= k:
                    return end


print(maxLength([1, 2, 3], 4))
print(maxLength([3, 1, 2, 1], 4))
