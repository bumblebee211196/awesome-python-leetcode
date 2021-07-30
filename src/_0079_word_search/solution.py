from typing import List


def solution(board: List[List[str]], word: str) -> bool:
    def helper(r, c, word, matrix):
        if not word:
            return True
        if 0 <= r < n and 0 <= c < m and matrix[r][c] == word[-1]:
            matrix[r][c] = "_"
            return (
                helper(r + 1, c, word[:-1], matrix)
                or helper(r - 1, c, word[:-1], matrix)
                or helper(r, c + 1, word[:-1], matrix)
                or helper(r, c - 1, word[:-1], matrix)
            )
        return False

    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if helper(i, j, word, board):
                return True
    return False
