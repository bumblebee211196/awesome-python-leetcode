from typing import List


def solution(candidates: List[int], target: int) -> List[List[int]]:
    def helper(idx, nums, total):
        if total == target:
            nonlocal res
            res.append(nums)
            return
        if total > target:
            return
        for i in range(idx, n):
            if i == idx or candidates[i] != candidates[i - 1]:
                helper(i + 1, nums + [candidates[i]], total + candidates[i])

    n = len(candidates)
    res = []
    candidates.sort()
    helper(0, [], 0)
    return res
