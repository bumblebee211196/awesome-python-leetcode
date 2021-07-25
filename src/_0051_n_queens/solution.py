from typing import List, Tuple


def solution1(n: int) -> List[List[str]]:
    board = [["." for _ in range(n)] for _ in range(n)]
    res = []

    def helper(r):
        if r == n:
            temp = []
            for row in board:
                temp.append("".join(row))
            res.append(temp)
            return
        for j in range(n):
            if board[r][j] == ".":
                board[r][j] = "Q"
                if checkQueen((r, j), board):
                    helper(r + 1)
                board[r][j] = "."

    helper(0)
    return res


def checkQueen(pos: Tuple[int, int], board: List[List[str]]) -> bool:
    r, c = pos
    n = len(board)
    # Check column
    for i in range(n):
        if i != r and board[i][c] == "Q":
            return False
    # Check upper-left diagonal
    i, j = r - 1, c - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    # Check upper-right diagonal
    i, j = r - 1, c + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    return True


def solution2(n: int) -> List[List[str]]:
    board = [["."] * n for _ in range(n)]
    cols = set()
    l_diag = set()
    r_diag = set()
    res = []

    def helper(row=0):
        if row == len(board):
            res.append(["".join(row) for row in board])
            return
        for col in range(len(board)):
            if col in cols or row - col in l_diag or row + col in r_diag:
                continue
            board[row][col] = "Q"
            cols.add(col)
            l_diag.add(row - col)
            r_diag.add(row + col)
            helper(row + 1)
            board[row][col] = "."
            cols.remove(col)
            l_diag.remove(row - col)
            r_diag.remove(row + col)

    helper()
    return res
