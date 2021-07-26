from typing import List


def solution(n: int) -> List[List[int]]:
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    x0 = y0 = 0
    x1 = y1 = n
    values = [v for v in range(1, (n * n) + 1)][::-1]
    while y1 > y0 and x1 > x0:
        for i in range(x0, x1):
            matrix[y0][i] = values.pop()
        for j in range(y0 + 1, y1 - 1):
            matrix[j][x1 - 1] = values.pop()
        if y1 != y0 + 1:
            for i in range(x1 - 1, x0 - 1, -1):
                matrix[y1 - 1][i] = values.pop()
        if x0 != x1 - 1:
            for j in range(y1 - 2, y0, -1):
                matrix[j][x0] = values.pop()
        y0 += 1
        y1 -= 1
        x0 += 1
        x1 -= 1
    return matrix
