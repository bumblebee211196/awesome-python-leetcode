from typing import List


def solution(nums: List[int]) -> int:
    unique = set(nums)
    for i in range(1, len(nums) + 2):
        if i not in unique:
            return i
