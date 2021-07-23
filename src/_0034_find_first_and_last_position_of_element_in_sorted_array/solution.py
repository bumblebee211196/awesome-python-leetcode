from typing import List


def solution(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    index = -1
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            index = m
        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1
    lres = index
    index = -1
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            index = m
        if nums[m] <= target:
            l = m + 1
        else:
            r = m - 1
    rres = index
    return [lres, rres]
