from typing import List


def solution(nums: List[int]) -> int:
    count = 0
    prev = None
    l = r = 0
    while r < len(nums):
        if prev is None:
            prev = nums[r]
            count = 1
        elif prev == nums[r]:
            count += 1
        else:
            count = 2 if count > 2 else count
            for _ in range(count):
                nums[l] = prev
                l += 1
            prev = nums[r]
            count = 1
        r += 1
    count = 2 if count > 2 else count
    if prev is not None:
        for _ in range(count):
            nums[l] = prev
            l += 1
    return l
