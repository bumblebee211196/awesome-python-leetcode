from typing import List


def solution(nums: List[int]) -> int:
    temp = nums.copy()
    nums.clear()
    nums.extend(list(set(temp)))
    nums.sort()
    return len(nums)
