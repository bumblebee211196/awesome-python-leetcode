from typing import List


def solution(nums: List[int]) -> int:
    curr_max = global_max = nums[0]
    for num in nums[1:]:
        curr_max = max(num, num + curr_max)
        global_max = max(global_max, curr_max)
    return global_max
