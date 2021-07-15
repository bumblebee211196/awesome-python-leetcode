from typing import List


def solution(nums: List[int], target: int) -> int:
    dist = float("inf")
    res = 0
    nums.sort()
    n = len(nums)
    for i in range(n):
        l, r = i + 1, n - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            diff = abs(target - total)
            if diff < dist:
                dist = diff
                res = total
            elif total > target:
                r -= 1
            else:
                l += 1
            if diff == 0:
                return res
    return res
