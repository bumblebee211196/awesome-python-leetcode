from typing import List


def solution(nums: List[int]) -> int:
    curr_reach = curr_max = jumps = 0
    for i, num in enumerate(nums[:-1]):
        curr_max = max(curr_max, i + num)
        if i == curr_reach:
            jumps += 1
            curr_reach = curr_max
    return jumps
