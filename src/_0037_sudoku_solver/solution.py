from typing import List


def solution(board: List[List[str]]):
    def is_valid(i, j, v):
        # Check column
        for c in range(N):
            if c != j and board[i][c] == v:
                return False
        # Check row
        for r in range(N):
            if r != i and board[r][j] == v:
                return False
        # Check 3 X 3 board
        rs = (i // 3) * 3
        cs = (j // 3) * 3
        for r in range(rs, rs + 3):
            for c in range(cs, cs + 3):
                if r != i and c != j and board[r][c] == v:
                    return False
        return True

    def solve():
        for i in range(N):
            for j in range(N):
                if board[i][j] == ".":
                    for v in range(1, 10):
                        v = str(v)
                        if is_valid(i, j, v):
                            board[i][j] = v
                            if solve():
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    N = 9
    solve()
    return board
