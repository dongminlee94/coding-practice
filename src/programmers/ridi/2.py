# -*- coding: utf-8 -*-


def solution(matrix):
    row_sum = []
    for mat in matrix:
        row_sum.append(sum(mat))

    col_sum = []
    for mat in zip(*matrix):
        col_sum.append(sum(mat))

    ans_sum = []
    for i in range(len(matrix)):
        sub_sum = []
        for j in range(len(matrix)):
            sub_sum.append(row_sum[i] + col_sum[j] - matrix[i][j])
        ans_sum.append(sub_sum)
    return ans_sum


assert solution(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[17, 19, 21], [23, 25, 27], [29, 31, 33]]
assert solution(matrix=[[1, 2, 1], [2, 3, 1], [3, 2, 1]]) == [[9, 9, 6], [10, 10, 8], [9, 11, 8]]
