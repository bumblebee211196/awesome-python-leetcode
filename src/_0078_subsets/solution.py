from typing import List


def solution(nums: List[int]) -> List[List[int]]:
    def helper(idx, curr):
        nonlocal res
        res.append(curr[:])
        for i in range(idx, len(nums)):
            curr.append(nums[i])
            helper(i + 1, curr)
            curr.pop()

    res = []
    helper(0, [])
    print(res)
    return res
