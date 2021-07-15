from typing import List


def solution(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n, res = len(nums), []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            diff = target - nums[i] - nums[j]
            l ,r = j + 1, n - 1
            while l < r:
                if nums[l] + nums[r] == diff:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif nums[l] + nums[r] < diff:
                    l += 1
                else:
                    r -= 1
    return res
