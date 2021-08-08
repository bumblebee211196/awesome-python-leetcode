from typing import List


def solution(nums: List[int], target: int) -> bool:
    new_nums = []
    seen = set()
    for num in nums:
        if num not in seen:
            new_nums.append(num)
            seen.add(num)
    nums = new_nums
    n = len(nums)
    l, r = 0, n - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return True
        elif nums[m] >= nums[l]:
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] <= target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return False
