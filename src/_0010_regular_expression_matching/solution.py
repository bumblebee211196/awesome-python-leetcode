from functools import lru_cache


def solution(s: str, p: str) -> bool:
    @lru_cache(None)
    def _isMatch(i, j):
        result = False
        if j == len(p):
            result = i == len(s)
        else:
            first_match = i < len(s) and p[j] in (s[i], ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                result = _isMatch(i, j + 2) or first_match and _isMatch(i + 1, j)
            else:
                result = first_match and _isMatch(i + 1, j + 1)
        return result

    return _isMatch(0, 0)
