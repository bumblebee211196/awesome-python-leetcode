from typing import List


def solution(nums: List[int]) -> None:
    l, m, r = 0, 0, len(nums) - 1
    while m <= r:
        if nums[m] == 0:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1
            m += 1
        elif nums[m] == 1:
            m += 1
        elif nums[m] == 2:
            nums[m], nums[r] = nums[r], nums[m]
            r -= 1
    return
