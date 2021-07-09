from typing import List


def solution(height: List[int]) -> int:
    m = max(height)
    l, r = 0, len(height) - 1
    res = 0
    while res < (r - l) * m:
        res = max(res, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res
