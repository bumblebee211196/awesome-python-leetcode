from typing import List


def solution(nums: List[int]) -> List[List[int]]:
    nums, n, res = sorted(nums), len(nums), []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, n - 1
        target = 0 - nums[i]
        while l < r:
            target_ = nums[l] + nums[r]
            if target_ < target:
                l += 1
            elif target_ > target:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res
