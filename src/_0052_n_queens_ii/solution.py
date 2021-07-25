def solution(n: int) -> int:
    board = [["."] * n for _ in range(n)]
    cols = set()
    l_diag = set()
    r_diag = set()
    res = 0

    def helper(row=0):
        if row == len(board):
            nonlocal res
            res += 1
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
