from typing import List


def solution(board: List[List[str]]) -> bool:
    for row in board:
        values = [value for value in row if value != "."]
        if len(values) != len(set(values)):
            return False
    
    for col in zip(*board):
        values = [value for value in col if value != "."]
        if len(values) != len(set(values)):
            return False
    
    for i in range(3):
        for j in range(3):
            if not is_valid_box(i, j, board):
                return False
    
    return True

def is_valid_box(r, c, board) -> bool:
    values = []
    for i in range(r * 3, (r + 1) * 3):
        for j in range(c * 3, (c + 1) * 3):
            if board[i][j] != ".":
                values.append(board[i][j])
    return len(values) == len(set(values))
    