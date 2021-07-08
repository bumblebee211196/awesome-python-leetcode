def solution(s: str) -> str:
        n = len(s)
        start = end = 0
        for i in range(n):
            l1 = helper(s, i, i)
            l2 = helper(s, i, i + 1)
            l = max(l1, l2)
            if l > end - start:
                start = i - ((l - 1) // 2)
                end = i + (l // 2)
        return s[start:end + 1]
    
def helper(s: str, l: int, r: int) -> int:
    n = len(s)
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1