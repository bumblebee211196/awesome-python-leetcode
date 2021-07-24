def solution(s: str, p: str) -> bool:
    i = j = 0
    n, m = len(s), len(p)
    pstar = stemp = None
    while i < n:
        if j < m and p[j] in ("?", s[i]):
            i += 1
            j += 1
        elif j < m and p[j] == "*":
            pstar = j
            stemp = i
            j += 1
        elif pstar is None:
            return False
        else:
            i = stemp + 1
            j = pstar + 1
            stemp = i
    return all(x == "*" for x in p[j:])
