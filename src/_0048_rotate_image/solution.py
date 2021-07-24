from typing import List


def solution(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for i, row in enumerate(matrix):
        matrix[i] = list(reversed(row))
