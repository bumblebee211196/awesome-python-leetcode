def solution(x: int) -> int:
    if x == 1:
        return 1
    l, r = 1, x // 2
    while l <= r:
        m = (l + r) // 2
        if m * m == x:
            return m
        elif m * m > x:
            r = m - 1
        else:
            l = m + 1
    return (l + r) // 2
