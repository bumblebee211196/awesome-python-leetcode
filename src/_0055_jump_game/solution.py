from typing import List


def solution(nums: List[int]) -> bool:
    n = len(nums)
    last = n - 1
    for i in range(n - 2, -1, -1):
        if i + nums[i] >= last:
            last = i
    return last == 0
