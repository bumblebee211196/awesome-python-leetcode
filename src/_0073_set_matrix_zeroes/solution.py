from typing import List


def solution(matrix: List[List[int]]) -> None:
    rows, cols = [], []
    m, n = len(matrix), len(matrix[0])
    to_set_zeros = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                to_set_zeros.append([i, j])
    for i, j in to_set_zeros:
        if j not in cols:
            for i_ in range(m):
                matrix[i_][j] = 0
            cols.append(j)
        if i not in rows:
            for j_ in range(n):
                matrix[i][j_] = 0
            rows.append(i)
