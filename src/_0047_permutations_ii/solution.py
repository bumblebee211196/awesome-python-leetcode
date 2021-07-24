from typing import List


def solution(nums: List[int]) -> List[List[int]]:
        
    def helper(nums_, res_):
        if not nums_:
            res.append(res_)
            return
        for i, num in enumerate(nums_):
            if i > 0 and nums_[i] == nums_[i - 1]:
                continue
            else:
                helper(nums_[:i] + nums_[i + 1:], res_ + [num])
    
    res = []
    nums.sort()
    helper(nums, [])
    return res
