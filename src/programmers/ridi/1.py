# -*- coding: utf-8 -*-


def solution(arrA, arrB):
    if len(arrA) != len(arrB):
        return False

    for _ in range(len(arrA)):
        if arrA == arrB:
            return True
        arrA = arrA[-1:] + arrA[:-1]
    return False


assert solution(arrA=[7, 8, 10], arrB=[10, 7, 8]) == True
assert solution(arrA=[4, 3, 2, 1], arrB=[5, 4, 1, 2]) == False
