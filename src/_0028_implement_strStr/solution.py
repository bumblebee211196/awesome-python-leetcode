def solution(haystack: str, needle: str) -> int:
    if needle:
        return haystack.find(needle)
    else:
        return 0
