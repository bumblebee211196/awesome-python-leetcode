from typing import List


def solution(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] >= nums[l]:
            if target >= nums[l] and target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if target >= nums[m] and target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1
