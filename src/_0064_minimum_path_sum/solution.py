from typing import List


def solution(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    for j in range(1, m):
        grid[0][j] += grid[0][j - 1]
    for i in range(1, n):
        grid[i][0] += grid[i - 1][0]
    for i in range(1, n):
        for j in range(1, m):
            grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
    return grid[-1][-1]
