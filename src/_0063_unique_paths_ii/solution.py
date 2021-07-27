from typing import List


def solution(obstacle_grid: List[List[int]]) -> int:
    if 1 in (obstacle_grid[0][0], obstacle_grid[-1][-1]):
        return 0
    n, m = len(obstacle_grid), len(obstacle_grid[0])
    matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    matrix[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if obstacle_grid[i - 1][j - 1] == 0:
                matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[-1][-1]
