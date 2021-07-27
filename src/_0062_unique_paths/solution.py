def solution(m: int, n: int) -> int:
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    matrix[1][1] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[-1][-1]
