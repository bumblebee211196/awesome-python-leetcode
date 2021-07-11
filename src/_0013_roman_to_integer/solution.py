def solution(s: str) -> int:
    mapper = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    n = len(s)
    for i in range(n):
        val = mapper[s[i]]
        if i != n - 1 and val < mapper[s[i + 1]]:
            res -= val
        else:
            res += val
    return res
