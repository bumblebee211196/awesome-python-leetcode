from typing import List


def solution(nums: List[int], val: int) -> int:
    new_index = 0
    for num in nums:
        if num != val:
            nums[new_index] = num
            new_index += 1
    for index in range(new_index, len(nums)):
        nums.pop()
    return len(nums)
