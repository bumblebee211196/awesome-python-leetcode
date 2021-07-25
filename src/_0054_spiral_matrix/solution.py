from typing import List


def solution(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    res = []
    y0 = 0
    y1 = len(matrix)
    x0 = 0
    x1 = len(matrix[0])
    while y1 > y0 and x1 > x0:
        for i in range(x0, x1):
            res.append(matrix[y0][i])
        for j in range(y0 + 1, y1 - 1):
            res.append(matrix[j][x1 - 1])
        if y1 != y0 + 1:
            for i in range(x1 - 1, x0 - 1, -1):
                res.append(matrix[y1 - 1][i])
        if x0 != x1 - 1:
            for j in range(y1 - 2, y0, -1):
                res.append(matrix[j][x0])
        y0 += 1
        y1 -= 1
        x0 += 1
        x1 -= 1
    return res
