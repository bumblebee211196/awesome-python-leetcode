from typing import List


def solution(a: List[int], b: int) -> List[int]:
    seen = {}
    for i, v in enumerate(a):
        diff = b - v
        if diff in seen:
            return [seen[diff], i]
        seen[v] = i
