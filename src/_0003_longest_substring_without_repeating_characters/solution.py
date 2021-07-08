def solution(s: str) -> int:
    seen = {}
    res = j = 0
    for i, c in enumerate(s):
        if c in seen:
            j = max(j, seen[c] + 1)
        seen[c] = i
        res = max(res, i - j + 1)
    return res
