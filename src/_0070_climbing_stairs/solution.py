def solution(n: int) -> int:
    if n <= 2:
        return n
    p1, p2 = 1, 0
    for _ in range(n):
        p1, p2 = p1 + p2, p1
    return p1
