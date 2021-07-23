def solution(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    idx, inc = 0, 1
    res = [""] * numRows
    for _, c in enumerate(s):
        res[idx] += c
        idx += inc
        if idx == 0 or idx == numRows - 1:
            inc *= -1
    return "".join(res)
