from typing import List


def solution(nums: List[int]) -> List[List[int]]:
    def helper(nums_, res_):
        if not nums_:
            nonlocal res
            res.append(res_[:])
            return
        for val in nums_:
            temp = nums_[:]
            temp.remove(val)
            res_.append(val)
            helper(temp, res_)
            res_.pop()

    res = []
    helper(nums, [])
    return res
