from typing import List


def solution(nums: List[int], target: int) -> int:
    n = len(nums)
    l, r = 0, n - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    if target > nums[l]:
        l += 1
    return l
